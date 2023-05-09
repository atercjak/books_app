from django.urls import path

from . import views

app_name = 'Books'

urlpatterns = [
    path('', views.upload_library, name='upload_library'),
    path('add', views.add_book, name='add_book'),

]
