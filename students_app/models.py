from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Student_Profile(models.Model):
    PREFIX = (
        ('Mr.', 'Mr.'),
        ('Ms.', 'Ms.'),
        ('Mrs.', 'Mrs.'),
    )

    prefix = models.CharField(null=True, max_length=4, choices=PREFIX, blank=True )
    first_name = models.CharField(max_length=50 )
    last_name = models.CharField(max_length=50, blank=True )
    phone = models.CharField(max_length=50, blank=True )
    email = models.CharField(max_length=50, blank=True )
    class_name = models.ForeignKey( 'class_app.Class_Profile', on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Subject_Score(models.Model):

    student = models.ForeignKey( Student_Profile, on_delete=models.CASCADE )
    class_name = models.ForeignKey( 'class_app.Class_Profile', on_delete=models.CASCADE, default=1 )

    subject = models.ForeignKey( 'class_app.Subject', models.CASCADE )
    score = models.IntegerField( default=0, validators=[MaxValueValidator(100), MinValueValidator(0)] )

    def __str__(self):
        return self.student.first_name
