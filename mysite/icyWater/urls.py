from django.conf.urls import url
from django.contrib.auth.views import login
from .import views
from .views import HomeView
app_name='isewat'
urlpatterns = [
url(r'^$',HomeView.as_view(),name = 'home'),
url(r"^login/$",login,{'template_name':'account/login.html'}),
url(r'^aboutme/$',views.aboutme,name = 'am'),

]
