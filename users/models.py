from django.db import models

class CustomUser(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username