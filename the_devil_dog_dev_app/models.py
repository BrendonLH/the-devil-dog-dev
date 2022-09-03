from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Service(models.Model):
    service_name = models.CharField(max_length=50)
    description = models.TextField(default='')
    image = models.ImageField(upload_to='images', default='')
    features = models.CharField(max_length=100, default='')
    time_to_completion = models.IntegerField(default=0)
    creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.service_name

    def get_absolute_url(self):
        return reverse('service_detail', args=[str(self.id)])
