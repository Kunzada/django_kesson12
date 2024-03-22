from django.db import models

# Create your models here.
class CustomUser(models.Model):
    class Status(models.TextChoices):
        admin='a','admin',
        user='u','user',

    fio=models.CharField(max_length=255)
    age=models.IntegerField()
    status=models.CharField(max_length=2, choices=Status.choices, 
                              default=Status.user)
    created_at=models.DateTimeField(auto_now_add=True)
