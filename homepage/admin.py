from django.contrib import admin
from .models import Students



class StudentsAdmin(admin.ModelAdmin):
    list_display = 'student_name', 'current_class', 'gender', 'dob'


admin.site.register(Students, StudentsAdmin)