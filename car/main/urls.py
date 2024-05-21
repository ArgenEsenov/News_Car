from django.urls import path
from .views import CarView, CarDetailView, CarCreateView, CarUpdateView, CarDeleteView

urlpatterns = [
    path('', CarView.as_view(), name='carView'),
    path('<int:pk>', CarDetailView.as_view(), name='carDetailView'),
    path('create/', CarCreateView.as_view(), name='carCreateView'),
    path('<int:pk>/update/', CarUpdateView.as_view(), name='carUpdateView'),
    path('<int:pk>/delete/', CarDeleteView.as_view(), name='carDeleteView'),
]
