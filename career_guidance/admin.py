from django.contrib import admin
from .models import StudentProfile, AcademicRecord, Interest, Career, CareerMatch

@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'education_level', 'school', 'major', 'created_at')
    search_fields = ('user__username', 'school', 'major')

@admin.register(AcademicRecord)
class AcademicRecordAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'score', 'semester')
    list_filter = ('semester', 'subject')

@admin.register(Interest)
class InterestAdmin(admin.ModelAdmin):
    list_display = ('student', 'category', 'level')
    list_filter = ('level', 'category')

@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    list_display = ('title', 'salary_range', 'market_demand')
    search_fields = ('title', 'description')

@admin.register(CareerMatch)
class CareerMatchAdmin(admin.ModelAdmin):
    list_display = ('student', 'career', 'match_score', 'created_at')
    list_filter = ('created_at',) 