from django.contrib import admin

from .models import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'profile_picture',
        'email_address',
        'phone_number',
        'room_number',
    )
    model = Teacher
