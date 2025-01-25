from django.urls import path
from myapp import views

urlpatterns=[
    path('',views.index,name='index'),
    path('sign-up/',views.signup,name='sign-up'),
    path('login_page/',views.login,name='login_page'),
    path('home/',views.home,name='home'),
    path('companyapply/<int:id>',views.companyapply,name='companyapply'),
    path('register/',views.register,name='register'),
]