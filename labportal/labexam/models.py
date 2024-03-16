from django.db import models

# Create your models here.
class CreateExam(models.Model):
    date = models.DateField()
    time = models.DurationField()
    subject_name = models.CharField(max_length=50)
    exam_name = models.CharField(max_length=50)
    faculty_name = models.CharField(max_length=50)
    have_file = models.BooleanField()
    file_upload = models.FileField(upload_to='labexam-data/', blank=True)
    student_files = models.BooleanField()
    student_files_upload = models.FileField(upload_to='labexam-data/student-uploads/', blank=True)

    def __str__(self):
        return f'{self.faculty_name} {self.exam_name} {self.date}'
    