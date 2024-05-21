from django.db import models


class Marka(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Model(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Car(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    year = models.PositiveIntegerField(default=1980)
    sold = models.BooleanField(default=False)
    marka = models.ForeignKey(to=Marka, on_delete=models.CASCADE)
    model = models.ForeignKey(to=Model, on_delete=models.CASCADE)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    author = models.CharField(max_length=16)
    text = models.TextField()
    create_time = models.DateTimeField(auto_now=True)
    car = models.ForeignKey(to=Car, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author} - {self.car}'
