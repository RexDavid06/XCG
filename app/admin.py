from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import DesignCategory, Design

User=get_user_model()

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']

class DesignAdmin(admin.ModelAdmin):
    list_display = ['picture', 'category']

class DesignCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


admin.site.register(User, UserAdmin)
admin.site.register(Design, DesignAdmin)
admin.site.register(DesignCategory, DesignCategoryAdmin)

