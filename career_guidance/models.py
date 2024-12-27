from django.db import models
from django.contrib.auth.models import User

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField()
    education_level = models.CharField(max_length=50)
    school = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username}'s profile"

    class Meta:
        db_table = 'student_profile'

class AcademicRecord(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    score = models.FloatField()
    semester = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-semester']
        db_table = 'academic_record'

class Interest(models.Model):
    INTEREST_LEVELS = [
        (1, 'Very Low'),
        (2, 'Low'),
        (3, 'Medium'),
        (4, 'High'),
        (5, 'Very High'),
    ]
    
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    category = models.CharField(max_length=50)
    level = models.IntegerField(choices=INTEREST_LEVELS)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'student_interest'

class Career(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    required_skills = models.JSONField()
    salary_range = models.CharField(max_length=50)
    market_demand = models.FloatField()  # 0-1 scale
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'career'
        
    def __str__(self):
        return self.title

class CareerMatch(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    career = models.ForeignKey(Career, on_delete=models.CASCADE)
    match_score = models.FloatField()
    academic_fit = models.FloatField()
    interest_fit = models.FloatField()
    market_fit = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'career_match'
        ordering = ['-match_score']