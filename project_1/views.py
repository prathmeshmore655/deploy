
from django.conf import settings
from django.http import HttpResponse
from pycurl import POST
from project_1.settings import BASE_DIR
from service.models import *
from django.shortcuts import get_object_or_404, render
from django.core.mail import send_mail,EmailMessage
from django.core.mail import EmailMessage


def home(request):
    return render(request,"home1.html")

def apply_for_concession(request):
    return render(request,"form1.html")

def about_us(request):
    return render(request,"about_us.html")

def admin_login(request):
    return render(request,"admin.html")
   

def instructions(request):
    return render(request,"Instructions.html")

def feedback(request):
    return render(request,"feedback.html")



def result(request):
    return render(request,"result.html")




     




def formdata(request):
    if request.method == "POST":
        registration_no = request.POST.get('registration')
        
       
        if students_registration_no.objects.filter(registration_no=registration_no).exists():
            
            first_name = request.POST.get('name').lower()
            middle_name = request.POST.get('father').lower()
            last_name = request.POST.get('surname').lower()
            mother_name = request.POST.get('mother').lower()
            date_of_birth = request.POST.get('dob').lower()
            academic_year = request.POST.get('year').lower()
            branch = request.POST.get('branch').lower()
            start_station = request.POST.get('start').lower()
            destination_station = request.POST.get('end').lower()
            section = request.POST.get('clas').lower()
            receipt = request.FILES.get('receipt')
            signature = request.FILES.get('sign')
            email = request.POST.get('email').lower()
            period = request.POST.get('period').lower()

            data = savedata(
                name=first_name,
                father=middle_name,
                surname=last_name,
                mother=mother_name,
                dob=date_of_birth,
                registration=registration_no,
                year=academic_year,
                branch=branch,
                start=start_station,
                end=destination_station,
                clas=section,
                receipt=receipt,
                signature=signature,
                email=email,
                period=period
            )

            data.save() 
        
            mail(request)

            return render(request, "successful.html")
        else:
            
            return HttpResponse("Invalid Registration No")
    else:
       
        return HttpResponse("Invalid Request Method")


def printtable(request):

    data=savedata.objects.all()

    if data:

        return render(request,'panel.html',{"form":savedata.objects.all()})
    
    else:
        
        return HttpResponse('Their is no data available')
    


def staff(request):

    return render(request,'staff.html',{"form":savedata.objects.all()})


def mail(request):    
    name = request.POST.get('name')
    email = request.POST.get('email') 
    message = f"{name}, your application form for applying concession was successfully submitted. Your concession receipt will be sent to your email,after approving the form."
    subject = "Confirmation Mail"

    send_mail(
        subject,
        message,
        '',
        [email],
        fail_silently=False
    )


def back(request):

    if request.method=='POST':
        f_email=request.POST.get('f_email')
        feedback=request.POST.get('new') 
        subject=f"Feedback Email BY {f_email}"
        email="2022ca32f@sigce.edu.in"
        

        send_mail(
            subject,
            feedback,
            '',
            [email],
            fail_silently=False
        )
        return render(request,'feedback.html')
    
    else:
        return render(request,'feedback.html')
    

            
def delete(request):
    key = request.POST.get('id')
    try:
        row = get_object_or_404(savedata, id=int(key))
        row.delete()
    except savedata.DoesNotExist:
        pass

    return render(request, 'panel.html', {"form": savedata.objects.all()})

        
def receipt(request):

    return render(request,'receipt.html',{"form":savedata.objects.all().order_by('-id')})





def form(request):

    if request.method=='POST':

        key = request.POST.get('key')

        data =savedata.objects.filter(pk=key)

        

        return render(request, 'print.html',{"info": data})

    else:

        pass

        





def send_receipt(request):
   
        stu_id=request.POST.get('id')

        print(stu_id)

        data=savedata.objects.filter(pk=stu_id)

        

        return render(request,'mail.html',{"data":data})
 



def approved(request):

    stu_id=request.POST.get('id')

    data=savedata.objects.filter(pk=stu_id)

    for item in data:

        new_data=approved_students(first_name=item.name, middle_name=item.father,last_name=item.surname,mother_name=item.mother,date_of_birth=item.dob,r_no=item.registration,receipt_file=item.receipt,sign=item.signature,e_year=item.year,department=item.branch,t_from=item.start,t_end=item.end,t_clas=item.clas,s_email=item.email)
        
        new_data.save()
    
    try:
        row = get_object_or_404(savedata, id=(stu_id))
        row.delete()
    except savedata.DoesNotExist:
        pass

    
    return printtable(request)


def show_mail(request):

    return render(request,'mail.html')


def mail_send(request):

    email = request.POST.get('r_email')
    attachment = request.FILES.get('attachment')
    email_subject = request.POST.get('subject')


    stu_id=request.POST.get('main')
        

    if attachment:
                email = EmailMessage(subject=email_subject, body='', to=[email])
                email.attach(attachment.name, attachment.read(), attachment.content_type)
                email.send()

                return delete_record(request,stu_id)
                
    else:
                return HttpResponse('No attachment provided.')


    
        
        






def delete_record(request,stu_id):  
        
        item=savedata.objects.get(pk=stu_id)


        new_data=approved_students(first_name=item.name, middle_name=item.father,last_name=item.surname,mother_name=item.mother,date_of_birth=item.dob,r_no=item.registration,receipt_file=item.receipt,sign=item.signature,e_year=item.year,department=item.branch,t_from=item.start,t_end=item.end,t_clas=item.clas,s_email=item.email)
        
        new_data.save()
    
        try:
            row = get_object_or_404(savedata, id=(stu_id))
            row.delete()
        except savedata.DoesNotExist:
            pass
        
        return HttpResponse('Email sent successfully.')

    

    
   

    






