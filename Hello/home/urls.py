from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path('', views.index, name='home' ),
    path('about', views.about, name='about' ),
    path('services', views.services, name='services' ),
    path('contact', views.contact, name='contact' ),
    path('delete/<int:id>/', views.delete_data, name='deletedata' ),
    path('/<int:id>/', views.update_data, name='updatedata' ),
    # path('update/<int:id>/', views.edit, name='edit' ),

]