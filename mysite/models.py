from django.db import models

from tinymce.models import HTMLField

class TestPage(models.Model):
    content1 = models.TextField()
    content2 = models.TextField()
    content = HTMLField(blank=True)

class TestInline(models.Model):
    page = models.ForeignKey(TestPage)
    content1 = models.TextField()
    content2 = models.TextField()
