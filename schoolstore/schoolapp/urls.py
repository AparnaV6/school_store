from . import views
from django.urls import path

app_name = 'schoolapp'
urlpatterns = [
    path('', views.home, name='home'),
    path('form/', views.form, name='form_page'),
    path('login/', views.login, name='login_page'),
    path('register/', views.register, name='register_page'),
    path('gs/', views.gs, name='gscience'),
    path('com/', views.com, name='commerce'),
    path('arts/', views.arts, name='arts'),
    path('astro/', views.astro, name='astro'),
    path('cs/', views.cs, name='cscience'),
    path('newpage/', views.newpage, name='new_page'),

]
