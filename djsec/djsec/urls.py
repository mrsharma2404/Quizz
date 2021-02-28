"""djsec URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from app1 import views
from django.urls import path,include
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu1/', views.homepage),   
    
#for user
    path('uupshow0/<str:stream>',views.upshow0),
    path('uupshow1/<str:quiz_name>',views.upshow1),
   
    

#for admin
    path('aloged/',views.alogged),   
    path('achoice/',views.achoice1),
    path('makequiz1/',views.aquiz),
    path('quizcal/',views.quizcalc),




    
     
    #path('makequiz1/',views.aquiz1),
    #path('makequizf/',views.aquizf), 




    #path('makequizf/',views.makequizf),
    #path('abt/', views.About),
    #path('adminlogin1/', views.adminlogin),
    #path('aa/',views.adata), #for entering detail in adm
    #path('sh/',views.ushow), #for showing data in user section


]
