from django.db import models
from django.core.validators import FileExtensionValidator


class UserProfile(models.Model):
    image = models.FileField(upload_to="images")


