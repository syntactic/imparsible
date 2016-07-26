#from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from models import Resume

# Create your views here.

"""def index(request):
    context = {"content" : "Hello World!"}
    return render(request, "resume/index.html", context)"""

class ResumeView(TemplateView):
    model = Resume
    template_name = "resume/index.html"

    def get_context_data(self, **kwargs):
        #context = super(ResumeView, self).get_context_data(**kwargs)
        context = {'resume' : Resume.objects.all()[0]}
        return context
