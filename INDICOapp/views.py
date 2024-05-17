from django.shortcuts import render,get_object_or_404,redirect
from .models import *
# Create your views here.

def homePage(request):
    settings_data = get_object_or_404(Setting, id=1)
    slider_data = Slider.objects.all().order_by('id')[:3]
    home_project_data = Project.objects.all().order_by('-id')[:4]  
    testmonial_data = Testimonial.objects.all()
    sponsor_data = Sponsor.objects.all()
    context = {
        'settings_data':settings_data,
        'slider_data':slider_data,
        'home_project_data':home_project_data,
        'testmonial_data':testmonial_data,
        'sponsor_data':sponsor_data,
    }
    return render(request, "index.html", context)


def allProject(request):
    settings_data = get_object_or_404(Setting, id=1)
    project_data = Project.objects.all()
    context = {
        'settings_data':settings_data,
        'project_data':project_data,
    }
    return render(request, "projects.html", context)


def singleProject(request,id):
    settings_data = get_object_or_404(Setting, id=1)
    single_pro = get_object_or_404(Project, id=id)
    context = {
        'settings_data':settings_data,
        'single_pro':single_pro,
    }

    return render(request, "project-single.html", context)



def servicePage(request):
    settings_data = get_object_or_404(Setting, id=1)
    service_data  = Service.objects.all()
    context = {
        'service_data':service_data,
        'settings_data':settings_data,
    }
    return render(request, "services-1.html", context)


def teamPage(request):
    settings_data = get_object_or_404(Setting, id=1)
    team = Team.objects.all()
    context = {
        'settings_data':settings_data,
        'team':team,
    }
    return render(request, "team.html", context)


def contactPage(request):
    settings_data = get_object_or_404(Setting, id=1)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = Contact()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.message = form.cleaned_data['message']
            data.save()
            return redirect('index')
    form = ContactForm
    context = {
        'settings_data':settings_data,
        'form':form,
    }
    return render(request, "contact.html", context)