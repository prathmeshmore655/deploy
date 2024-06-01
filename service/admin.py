from django.contrib.admin.sites import site
from service.models import *
from django.contrib import admin


class ServiceAdmin(admin.ModelAdmin):
    list_display=('id','name','father','surname','mother','dob','registration','year','branch','start','end','clas','receipt','signature','email')
    search_fields=['name','registration','branch','start','clas','year','surname','email']


class register_table(admin.ModelAdmin):
    list_display=('id','registration_no','student_name')
    search_fields=['registration_no','student_name']

class approved_table(admin.ModelAdmin):

    list_display=('id','first_name','middle_name','last_name','mother_name','e_year','r_no','receipt_file','sign','t_from','t_end')
    search_fields=['first_name','middle_name','last_name','r_no','t_from','t_end']


admin.site.site_header="College Concession Website"
admin.site.register(savedata,ServiceAdmin)
admin.site.register(students_registration_no,register_table)
admin.site.register(approved_students,approved_table)
