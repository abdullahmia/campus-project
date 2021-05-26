from django.contrib import admin
from .models import UserTrack

class UserTrackAdmin(admin.ModelAdmin):
    list_display = ['fname', 'lname', 'gender', 'phone_number', 'email', 'nid']
    list_display_links = ['fname', 'lname']
    list_editable = ['gender']
    list_filter = ['gender']
    list_per_page = 20


admin.site.register(UserTrack, UserTrackAdmin)