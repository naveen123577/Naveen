from django.urls import path

from main.views import home,contact,about,certificate

app_name='main'

urlpatterns = [
    path('', home,name='home'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('certificate/', certificate,name='certificate'),

]
