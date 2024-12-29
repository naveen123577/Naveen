from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

# def contact(request):
#     return render(request,'contact.html')


def about(request):
    return render(request,'about.html')


from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render

def contact(request):
    if request.method == "POST":
        # Get form data
        name = request.POST.get('name')
        from_email = request.POST.get('from_email')
        phone_number = request.POST.get('phone_number')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Set your default "To" address here
        to_email = 'spiceexdummy@gmail.com'

        # Compose the email message with name, phone number, and from_email
        full_message = f"Name: {name}\nEmail: {from_email}\nPhone Number: {phone_number}\n\n{message}"

        # Send email
        send_mail(subject, full_message, settings.EMAIL_HOST_USER, [to_email], fail_silently=False)

        # Display success message
        messages.success(request, "Mail sent successfully...")

    return render(request, "contact.html")

# def mailing(request):
#     if request.method=="POST":
#         eml=request.POST.get('em')
#         sbj=request.POST.get('sb')
#         msg=request.POST.get('msg')
#         send_mail(sbj,msg,settings.EMAIL_HOST_USER,[eml],fail_silently=False)
#         messages.success(request,"Mail send successfully...")
#     return render(request,"email.html")
def certificate(request):
    return render(request,'certificate.html')