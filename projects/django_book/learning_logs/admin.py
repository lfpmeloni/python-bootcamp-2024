from django.contrib import admin # type: ignore
from .models import Topic, Entry

# Register your models here.

admin.site.register(Topic)
admin.site.register(Entry)