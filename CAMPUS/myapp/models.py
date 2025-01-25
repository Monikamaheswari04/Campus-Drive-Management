from django.db import models

# Create your models here.

class Userdata(models.Model):
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

    def __str__(self): 
        return self.email 

class Companyinfo(models.Model):
    company_name=models.CharField(max_length=100)
    campany_image=models.ImageField(upload_to='campanies/')
    job_position=models.CharField(max_length=100)


    def __str__(self):
        return self.company_name

class Register(models.Model):
    c_name=models.CharField(max_length=100)    
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    gender=models.CharField(max_length=100)
    contact=models.IntegerField()
    resume=models.CharField(max_length=100)

    def __str__(self):
        return self.p_name