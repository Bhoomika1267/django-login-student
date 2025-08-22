from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'age', 'course', 'enrollment_number', 'is_active')
    search_fields = ('name', 'email', 'course')
    list_filter = ('course', 'is_active')
