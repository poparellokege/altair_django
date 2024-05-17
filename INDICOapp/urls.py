from django.urls import path 
from  INDICOapp.views import *

urlpatterns = [
    path('', homePage, name='index'),
    path('projects/', allProject, name="all-projects"),
    path('project_details/<int:id>/', singleProject, name="single-project"),
    path('service/', servicePage, name="service"),
    path('team/', teamPage, name="team"),
    path('contact/', contactPage, name="contact"),
]