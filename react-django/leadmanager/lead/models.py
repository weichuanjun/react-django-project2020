from django.db import models

# Create your models here.


class Lead(models.Model):
    name = models.models.CharField(max_length=50)
    email = models.models.EmailField(max_length=254, unique=True)
    message = models.models.CharField(_(""), max_length=50, blank=True)
    creat_at = models.models.DateTimeField(_(""),  auto_now_add=True)
