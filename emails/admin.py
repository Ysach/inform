from django.contrib import admin
import models
# Register your models here.


class APIServerAdmin(admin.ModelAdmin):
    list_display = ('send_user', 'email_subject', 'to_email', 'email_content', 'phone_number', 'phone_content', 'send_time')
    search_fields = ('send_user', 'to_email', 'phone_number')
    list_filter = ('send_user', 'to_email', 'phone_number')


class APIUserAdmin(admin.ModelAdmin):
    list_display = ('user_email', 'user_phone', 'create_time')
    search_fields = ('user_email', 'user_phone')
    list_filter = ('user_email', 'user_phone')

admin.site.register(models.APIUser, APIUserAdmin)
admin.site.register(models.APIServer, APIServerAdmin)
