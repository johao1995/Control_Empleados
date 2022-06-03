from django.shortcuts import render
from django.views import generic 

class HomePage(generic.TemplateView):
    template_name='home.html'

    def get_context_data(self,*args,**kwargs):
        context=super().get_context_data(*args,**kwargs)
        context['title']='Home'
        return context