from django.contrib import admin
from .models import Student,User

# Register your models here.

admin.site.register(User)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll_no','city','state']