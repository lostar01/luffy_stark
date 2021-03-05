"""luffy_stark URL Configuration

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
from django.urls import path
from stark.service.v1 import site


# print(site.urls)

"""
[
  {'model_class': <class 'app01.models.Depart'>, 'handler': <app01.stark.DepartHandler object at 0x7faf8e5e4710>}, 
  {'model_class': <class 'app01.models.UserInfo'>, 'handler': <app01.stark.UserInfoHandler object at 0x7faf8e5e47f0>}, 
  {'model_class': <class 'app02.models.Host'>, 'handler': <app02.stark.HostHandler object at 0x7faf8e5e4cf8>}
]

"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('stark/',site.urls),

]
