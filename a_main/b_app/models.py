from django.db import models

# Create your models here.

class Departmet(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    


class Section(models.Model):
    name=models.CharField(max_length=100)
    department=models.ForeignKey(Departmet,on_delete=models.CASCADE)
    def __str__(self):
        return  self.name
    

class Student(models.Model):
    departmrct=models.ForeignKey(Departmet,on_delete=models.CASCADE)
    section=models.ForeignKey(Section,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField(unique=True)
    roll=models.IntegerField(max_length=3)

    def __str__(self):
        return self.name





