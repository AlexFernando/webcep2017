from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import RegistrationForm,ContactForm

# Create your views here.

def index(request):
    if request.method == "POST":
        register_form = RegistrationForm (request.POST)#haciendo post del form
        if register_form.is_valid():
            register_form.save()
            return render(request, 'homepage/success_register.html', {
                'msg_register': register_form.data['name'] + ', hemos registrado tus datos con exito'})
    else:
        register_form = RegistrationForm()
    return render(request, 'homepage/home.html', {'form_register': register_form})

def contact(request):
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
                send_mail(subject,from_email,message,['alexf@localhost.com'])
            except BadHeaderError:
                return HttpResponse('Sus datos no se han guardado.')

            return redirect('success')

    return render(request, 'homepage/contact_us.html', {'form_contact': contact_form})

def success(request):
    return render(request,"homepage/success.html")
