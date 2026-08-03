from django.db import models
from django.contrib import admin
from django.urls import reverse

# Create your models here.
#st_id, fname, lname

PREFIX_NAME = (
    ("นาย", "นาย"),
    ("นาง", "นาง"),
    ("นางสาว", "นางสาว"),
)


class Student(models.Model):

    prefix = models.CharField(max_length=10, choices=PREFIX_NAME, default="นาย")
    st_id = models.CharField(max_length=12, unique=True)
    fname = models.CharField(max_length=100, blank=False)
    lname = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.prefix + " " + self.fname + " " + self.lname + " [" + self.st_id + "]"

    def get_absolute_url(self):
        return reverse('student_detail', kwargs={'pk': self.pk})


class StudentAdmin(admin.ModelAdmin):
    list_display = ('st_id', 'prefix', 'fname', 'lname')

