from django.conf.urls import url
from django.contrib.auth.views import login
from .import views
app_name='isewat'
urlpatterns = [
url(r'^$',views.home),
url(r"^login/$",login,{'template_name':'account/login.html'}),
url(r'^aboutme/$',views.aboutme,name = 'am'),

]
