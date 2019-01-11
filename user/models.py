from django.db import models
from django.urls import reverse

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=5)
    last_name = models.CharField(max_length=5)
    first_name_kana = models.CharField(max_length=10)
    last_name_kana = models.CharField(max_length=10)
    
    birth_date = models.DateField()
    
    phone = models.CharField(max_length=11)
    
    zip_code = models.CharField(max_length=7)
    region = models.ForeignKey(
        'region.Region',
        on_delete=models.PROTECT
    )
    address = models.CharField(max_length=255)
    
    comment = models.CharField(max_length=255, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (self.last_name + self.first_name)

    def get_absolute_url(self):
        return reverse('user:detail', kwargs={'pk': self.pk})
