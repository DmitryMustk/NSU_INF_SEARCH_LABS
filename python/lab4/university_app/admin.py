from django.contrib import admin
from .models import University, Student

class UniversityAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_name', 'full_name', 'creation_date')
    search_fields = ('short_name', 'full_name')
    list_filter = ('creation_date',)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'university', 'enrollment_year', 'birth_date')
    search_fields = ('full_name',)
    list_filter = ('university', 'enrollment_year')

admin.site.register(University, UniversityAdmin)
admin.site.register(Student, StudentAdmin)
