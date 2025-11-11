from django.urls import path 
from finc import views  


urlpatterns = [
    path("",views.home,name='home'),
    path("register/",views.register,name='register'),
    path("dashboard/",views.dashboard,name='dashboard'),
    path("login/",views.login,name='login'),
    path('open-account/', views.open_account, name='open_account'),
 

    path("deposit/",views.deposit,name='deposit'),
    path("withdraw/",views.withdraw,name='withdraw'),

    
]
