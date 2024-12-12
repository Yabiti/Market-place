from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path("", include(('core.urls'))),
    path('contact/', views.contact, name="contact")

]