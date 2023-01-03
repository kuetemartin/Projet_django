from django.urls import path

from .views import home,about,descr

urlpattern = [
    path('home/', home),
    path('about/',about ),
    path('description/',descr ),
]

