from django.contrib import admin

from .models import Student, Teacher, StudentPosition


class StudentPositionInline(admin.TabularInline):
    model = StudentPosition
    extra = 1


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id']
    inlines = [StudentPositionInline, ]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'subject']
    list_filter = ['name']
