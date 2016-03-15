from django.core.urlresolvers import reverse
from django.contrib import admin

from .models import TestPage, TestInline
from tinymce.widgets import TinyMCE


class TinyMCETestPageAdmin(admin.ModelAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in ('content1', 'content2'):
            return db_field.formfield(widget=TinyMCE(
                attrs={'cols': 80, 'rows': 30},
            ))
        return super(TinyMCETestPageAdmin, self).formfield_for_dbfield(db_field, **kwargs)


admin.site.register(TestPage, TinyMCETestPageAdmin)
