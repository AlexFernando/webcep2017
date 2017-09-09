from django.http import Http404, HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render,redirect
from .forms import RegistrationForm,ContactForm
from django.contrib import messages


# Create your views here.

#view for handling Register form
def index(request):
    contact_form = ContactForm
    if request.method == "POST":
        registration_form = RegistrationForm (request.POST)
        if registration_form.is_valid():
            registration_form.save()
            return render(request, 'homepage/success_register.html', {
                'msg_register': registration_form.data['name'] + ', hemos registrado tus datos con exito'})

    else:
        registration_form = RegistrationForm()
    return render(request, 'homepage/home.html', {'form_register': registration_form, 'form_contact':contact_form})

#for handling contact form email
def contact(request):
    registration_form = RegistrationForm()
    if request.method == 'GET':
        contact_form = ContactForm()

    else:
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            #name = contact_form.cleaned_data['name']
            subject = contact_form.cleaned_data['subject']
            from_email = contact_form.cleaned_data['from_email']
            message = contact_form.cleaned_data['message']

            try:
                send_mail(subject,message,from_email,['cep.201x@gmail.com'])

            except BadHeaderError:
                return HttpResponse('Sus datos no se han guardado.')

            return redirect('success')

    return render(request, 'homepage/contact_us.html', {'form_contact': contact_form, 'form_register':registration_form})

def success(request):
    return render(request,"homepage/success.html")

