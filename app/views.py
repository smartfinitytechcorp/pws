from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.views import generic
from .forms import *
from .models import *
import csv, io
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.template import Template
# one parameter named request
@login_required(login_url='/admin/login/?next=/admin/')
def profile_upload(request):
    # declaring template
    template = "profile_upload.html"
    data = Review.objects.all()
# prompt is a context variable that can have different values      depending on their context
    prompt = {
        'profiles': data    
              }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string,):
        _, created = Review.objects.update_or_create(
            name=column[0],
            title=column[2],
            rating=column[4],
            rating_img=column[5],
            description=column[3],
            order_id=column[1]
        )
    context = {}
    return render(request, template, context)


# Create your views here.

# class WritingView(generic.FormView):
#     model = WritingModel
#     form_class = writingForm
#     template_name = 'home.html'
#     # success_url = '/'
#     def form_valid(self, form):
#         if form.is_valid():
#             form.save()
#             messages.success(self.request, 'Form submission successful')
#             return HttpResponseRedirect(self.request.path_info)
#         return super().form_valid(form)

def WritingModel(request):
    if request.method == 'POST':
        contact_form = writingForm(request.POST)
        if contact_form.is_valid():
                contact_form.save()
                name = contact_form.cleaned_data['name']
                email = contact_form.cleaned_data['email']
                phone = contact_form.cleaned_data['phone_number']
               
                from django.core.mail import EmailMultiAlternatives
                text_content = ''
                html_content = "<strong>Name: </strong> <span>{}</span><br>  <strong>Email: </strong><span>{}</span><br>  <strong>Phone:</strong><span>{}</span>".format(name,email,phone)
                msg = EmailMultiAlternatives('Perfect Writing Solution Form Submision', text_content, settings.EMAIL_HOST_USER, ['elijahmurphy2428@gmail.com'])
                msg.attach_alternative(html_content, "text/html")
                msg.send() 
                messages.success(request,'Form submission successful')
                return redirect('/thankyou')
    else:
        contact_form = writingForm()
    reviews = Review.objects.all()
    return render(request, 'home.html', {
        'contact_form': writingForm,
        'reviews': reviews,
    })

def All_reviews(request):
    reviews = Review.objects.all()
    return render(request, 'reviews.html', {
        'reviews': reviews,
    })

def Subscribe(request):
    # if request.method == 'GET':
    #     return render(request,'home.html')
    # if request.method == 'POST':
    #     email = request.POST.get('email')
    #     if not email is None:
    #             newsletter_response = newsletter.objects.create(newsletter_field=email)
    #             newsletter_response.save()
    #             messages.success(request,'Form submission successful')
    #     return render(request,'home.html')


    if request.method == 'GET':
        return render(request,'home.html')

    if request.method == 'POST':
        print("*****************************************")
        name= request.POST.get('email')
        if not name is None:
            newsletter_response = newsletter.objects.create(newsletter_field=name)
            newsletter_response.save()
            messages.success(request,'Thankyou For Subscribing')
        return redirect(request.path)

    


    

# def get_thank_you(request):
#     return render(request, "apps/ThankU.html")