from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from foto.models import Categoria, Galleria, TaggedGalleria


# Register your models here.
class TaggedGalleriaAdmin(admin.ModelAdmin):
    list_display = ["id", "content_object_id"]

# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ["name"]
    prepopulated_fields = {'slug': ('name',)}

# Register your models here.
class GalleriaAdmin(admin.ModelAdmin):
    list_display = ["id", "description", "image"]


class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'last_name',
                    'is_staff', 'last_login')  # Added last_login

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Galleria, GalleriaAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(TaggedGalleria, TaggedGalleriaAdmin)
