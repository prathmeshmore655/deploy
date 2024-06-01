import datetime
from django.db import models
from traitlets import default

def get_default_email():
    return 'example@example.com'

class savedata(models.Model):
    name = models.CharField(max_length=20)
    father = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    mother = models.CharField(max_length=20)
    dob = models.CharField(max_length=20)
    registration = models.CharField(max_length=9)
    receipt = models.FileField(upload_to="images/",default='None')
    signature = models.FileField(upload_to="signature/",default='None')
    year = models.CharField(max_length=20)
    branch = models.CharField(max_length=30)
    start = models.CharField(max_length=20)
    end = models.CharField(max_length=20)
    clas = models.CharField(max_length=20)
    email = models.EmailField(max_length=50,default=get_default_email)
    submit_time=models.DateTimeField(auto_now_add=True)
    period=models.CharField(max_length=30,default='none')




    

    class Meta:
        ordering = ['-submit_time'] 





class students_registration_no(models.Model):
    registration_no=models.CharField(max_length=9)
    student_name=models.CharField(max_length=50)


    
class approved_students(models.Model):
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    mother_name = models.CharField(max_length=20)
    date_of_birth = models.CharField(max_length=20)
    r_no = models.CharField(max_length=9)
    receipt_file = models.FileField(upload_to="approved_media",default='None')
    sign = models.FileField(upload_to="approved_media",default='None')
    e_year = models.CharField(max_length=20)
    department = models.CharField(max_length=30)
    t_from = models.CharField(max_length=20)
    t_end = models.CharField(max_length=20)
    t_clas = models.CharField(max_length=20)
    s_email = models.EmailField(max_length=50,default=get_default_email)
    




