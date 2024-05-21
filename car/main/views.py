from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import CarForm
from .models import Car, Category


class CarView(ListView):
    model = Car
    template_name = 'car_list.html'
    context_object_name = 'cars'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        category = self.request.GET.get('category')

        if category:
            category_object = Category.objects.get(name=category)
            queryset = Car.objects.filter(category=category_object)
        else:
            queryset = Car.objects.all()

        if query:
            queryset = queryset.filter(title__icontains=query)

        return queryset

class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'
    context_object_name = 'cars'


class CarCreateView(CreateView):
    model = Car
    template_name = 'car_form.html'
    form_class = CarForm
    success_url = reverse_lazy('carView')

    def form_valid(self, form):
        return super().form_valid(form)


class CarUpdateView(UpdateView):
    model = Car
    template_name = 'car_form.html'
    form_class = CarForm

    def get_success_url(self):
        return reverse_lazy('carDetailView', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        return super().form_valid(form)


class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = reverse_lazy('carView')

