from django.contrib import admin , messages
from django.shortcuts import render
from django.http import HttpResponse , FileResponse
from django.core import serializers
import json

# Register your models here.
from .models import Post









def export_as_json(modeladmin, request, queryset):
    data = serializers.serialize("json", queryset)
    response = HttpResponse(content_type="application/json")
    response['Content-Disposition'] = 'attachment; filename="posts.json"'
    response.write(data)
    return response




def make_published(modeladmin , request , queryset) :

    result = queryset.update(status = 'published')

    if result == 1 :
        message_bit  = "1 post was "
    else :
        message_bit = "{} posts were".format(result)

    modeladmin.message_user(request , "{} successfully marked as published".format(message_bit))    



def make_draft(modeladmin , request , queryset) :

    result = queryset.update(status = 'draft') 

    if result == 1 :
        message_bit  = "1 post was "
    else :
        message_bit = "{} posts were".format(result)

    modeladmin.message_user(request , "{} successfully marked as draft".format(message_bit))    
   


make_published.short_description = 'Mark selected posts as published'
make_draft.short_description = 'Mark selected posts as drafted'
export_as_json.short_description = 'Mark Selected psots as json request'



@admin.register(Post)
class PostAdmin(admin.ModelAdmin) :
    list_display = ('title','slug','publish','status')
    list_filter = ('publish','status')
    search_fields = ('title' , 'body')
    ordering = ['status','publish']
    prepopulated_fields = {'slug' : ('title',)}
    actions = [make_published , make_draft , export_as_json]


    def index(self, request, extra_context=None):

        extra_context = extra_context or {}

        extra_context['welcome_link'] = '/welcome/'

        return super().index(request, extra_context)


