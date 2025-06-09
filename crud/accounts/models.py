from django.db import models
from django.utils import timezone

class Book(models.Model):
    book_name = models.CharField(max_length=100, blank=False, null=False)
    book_desc = models.TextField(blank=False, null=False)
    book_image = models.ImageField(upload_to='media/books/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.book_name

