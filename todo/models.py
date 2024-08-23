import uuid
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Todo(models.Model):
  id = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=255)
  description = models.TextField(blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return self.title