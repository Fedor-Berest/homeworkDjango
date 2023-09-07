from django.contrib import admin
from .models import Advertisement

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title', 'description', 'created_date', 'update_date', 'auction', 'get_html_img']
    list_filter = ['created_at', 'auction']

admin.site.register(Advertisement, AdvertisementAdmin)


# Register your models here.
