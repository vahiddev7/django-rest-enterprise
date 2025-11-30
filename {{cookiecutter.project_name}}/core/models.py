from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class BaseModel(models.Model):
    created_at = models.DateTimeField(verbose_name=_("created_at"), default=timezone.now())
    updated_at = models.DateTimeField(verbose_name=_("updated_at"), auto_now=True)
    