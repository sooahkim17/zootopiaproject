from disney import views
from django.urls import path
urlpatterns=[
    path('show/',views.show,name='show'),
    path('post/',views.post,name='post'),
]