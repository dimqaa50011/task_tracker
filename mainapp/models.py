from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


class Task(models.Model):
    body = models.CharField(
        verbose_name=_('Body'),
        max_length=1024,
    )
    created_at = models.DateTimeField(
        _('date created'), auto_now_add=True
    )
    updated_at = models.DateTimeField(
        _('date updated'), auto_now=True
    )
    
    def get_absolute_url(self):
        return reverse("mainapp:new_task", kwargs={"pk": self.pk})
    
