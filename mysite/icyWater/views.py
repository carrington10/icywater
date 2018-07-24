from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Song
# Create your views here.

class HomeView(TemplateView):
      template_name="home.html"
      def get(self,request):
                    songs = Song.objects.all().order_by('-created')
                    args = {
                            'songs':songs
                        }
                    return render(request, self.template_name, args)

def aboutme(request):
    return render(request,'aboutme.html');
