from django.db import models

# Create your models here.

class Departmet(models.Model):
    dep_name=models.CharField(max_length=100)
    def __str__(self):
        return self.dep_name    


class Section(models.Model):
    sec_name=models.CharField(max_length=100)
    department=models.ForeignKey(Departmet,on_delete=models.CASCADE)
    def __str__(self):
        return  self.sec_name
    

class Student(models.Model):
    departmrct=models.ForeignKey(Departmet,on_delete=models.CASCADE)
    section=models.ForeignKey(Section,on_delete=models.CASCADE)
    stu_name=models.CharField(max_length=100)
    stu_age=models.IntegerField()
    stu_email=models.EmailField(unique=True)
    roll=models.IntegerField(max_length=3)

    def __str__(self):
        return self.stu_name





