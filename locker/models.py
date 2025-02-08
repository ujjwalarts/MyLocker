from django.contrib.auth.models import User
from django.db import models
import uuid

class Document(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='documents/')  # Store files in the 'documents/' folder
    uploaded_at = models.DateTimeField(auto_now_add=True)
    verified = models.BooleanField(default=False)

class SharedDocument(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    shared_with = models.EmailField()
    access_key = models.CharField(max_length=50, default=uuid.uuid4)
    shared_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.document.title} shared with {self.shared_with}"
