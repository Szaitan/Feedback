from django.db import models
from django.core.validators import FileExtensionValidator


class UserProfile(models.Model):
    image = models.ImageField(upload_to="images")


