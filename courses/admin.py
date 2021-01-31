from django.contrib import admin

# Register your models here.

from .models import Course, Review


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'active', 'created_at', 'updated_at')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('course', 'name', 'email', 'review',
                    'active', 'created_at', 'updated_at')
