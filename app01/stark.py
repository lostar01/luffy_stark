from django.conf.urls import url
from django.urls import reverse

from stark.service.v1 import site,StarkHandler
from app01 import models
from django.shortcuts import HttpResponse
class DepartHandler(StarkHandler):
        pass


class UserInfoHandler(StarkHandler):
        def extra_urls(self):
                return  [
                        url('^detail/(\d+)/$',self.change_detail ),
                ]

        def change_detail(self,request,pk):

                return HttpResponse("详细页面")


site.register(models.Depart,DepartHandler)
site.register(models.UserInfo,UserInfoHandler)