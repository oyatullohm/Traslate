from django.contrib import admin

# Register your models here.
from .models import Trans

@admin.register(Trans)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id',"uz","en","ru"]
    search_fields = ['uz']
