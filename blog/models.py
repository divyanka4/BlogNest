from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
# Create your models here.

from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = CKEditor5Field(config_name='default')
    author = models.CharField(max_length=100)
    published_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    

class ContactMessage(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"
