from django.urls import path
from djangoApp import views


urlpatterns=[

    path('',views.home,name="my_index"),
    path('about/',views.about,name="my_about"),
    path('contact/',views.contact,name="my_contact"),
    path('blog/',views.blog,name="my_blog"),
    path('services/',views.services,name="my_services"),

]
