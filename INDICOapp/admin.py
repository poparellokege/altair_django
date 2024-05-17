from django.contrib import admin
from INDICOapp.models import *
# Register your models here.

class SliderAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_tag', 'created_at', 'updated_at']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','image_tag','created_at', 'updated_at']
    list_filter = ['status', 'created_at']
    prepopulated_fields = {'slug':('title',)}


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title','image_tag', 'category','status','created_at','updated_at']
    list_filter = ['status', 'created_at']
    prepopulated_fields = {'slug':('title',)}


class TeamAdmin(admin.ModelAdmin):
    list_display = ['name','image_tag','status','created_at','updated_at']
    list_filter = ['name']    


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','status','created_at','updated_at']
    list_filter = ['name']      


admin.site.register(Contact,ContactAdmin)
admin.site.register(Team,TeamAdmin)
admin.site.register(Project,ProjectAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Slider,SliderAdmin)   
admin.site.register(Setting)
admin.site.register(Service)
admin.site.register(Sponsor)
admin.site.register(Testimonial)


