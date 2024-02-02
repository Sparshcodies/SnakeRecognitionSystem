
from django.urls import path
from snake_app.views import *
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'snake_app'

urlpatterns = [
    path('',welcome,name='Welcome'),
    path('second',second,name='second'),
    path('submit',submit,name='submit'),
    # ... other URL patterns ...
]

