from django.urls import path

from . import views

app_name = 'Books'

urlpatterns = [
    path('import/', views.upload_library, name='upload_library'),

]
