from django.urls import path
from . import views


urlpatterns = [
    path('', views.Hi,name = 'HomePage'),
    path('about', views.about,name = 'about'),
    path('gallary', views.gallary,name = 'gallary'),
    path('contact', views.contact,name = 'contact'),

]

