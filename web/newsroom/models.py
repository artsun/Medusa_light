from uuid import uuid4
from django.utils import timezone

from django.db import models
from django.utils.translation import gettext_lazy as _


class News(models.Model):
    id = models.UUIDField(db_column='id', primary_key=True, default=uuid4, editable=False, unique=True, blank=True)
    subject = models.CharField(_('subject'), max_length=256, unique=True, blank=False)
    content = models.TextField(_('content'), null=True, blank=True)
    date = models.DateField(_('date'), default=timezone.now, editable=True, blank=True)  # мб также auto_now_add=True
    # в задании указано, что значение даты должно быть настраиваемым

    class Meta:
        verbose_name = _('news')
        verbose_name_plural = _('news')
        db_table = 'newsroom\".\"news'

    def __str__(self):
        return self.subject
