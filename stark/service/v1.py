from django.conf.urls import url
from django.shortcuts import HttpResponse,render

class StarkHandler(object):
    def __init__(self, model_class,prev):
        self.model_class = model_class
        self.prev = prev

    def changelist_view(self, request):
        """
        访问: http://192.168.137.170:8000/stark/app02/role/list/  model_class: app02.models.Role
        访问: http://192.168.137.170:8000/stark/app01/depart/list/  model_class: app01.models.Depart
        访问: http://192.168.137.170:8000/stark/app01/userinfo/list/  model_class: app01.models.UserInfo
        """
        data_list = self.model_class.objects.all()
        # return HttpResponse("列表页面",data_list)
        print(data_list)
        return render(request,'stark/changelist.html',{"data_list": data_list})

    def add_view(self, request):

        return HttpResponse("添加页面")

    def change_view(self, request, pk):

        return HttpResponse("编辑页面")

    def delete_view(self, request, pk):
        return HttpResponse("删除页面")

    def get_url_name(self,param):
        app_label, model_name = self.model_class._meta.app_label, self.model_class._meta.model_name
        if self.prev:
            return "%s_%s_%s_%s" %(app_label,self.prev,model_name,param)

        return "%s_%s_%s" % (app_label, model_name, param)

    @property
    def get_list_url_name(self):
        return self.get_url_name("list")

    @property
    def get_add_url_name(self):
        return self.get_url_name("add")

    @property
    def get_edit_url_name(self):
        return self.get_url_name("edit")

    @property
    def get_delete_url_name(self):
        return self.get_url_name("delete")

    def get_urls(self):
        patterns = [
            url('^list/$' ,self.changelist_view,name=self.get_list_url_name ),
            url('^add/$', self.add_view,name=self.get_add_url_name ),
            url('^edit/(\d+)/$', self.change_view,name=self.get_edit_url_name ),
            url('^del/(\d+)/$', self.delete_view,name=self.get_delete_url_name)
        ]
        patterns.extend(self.extra_urls())

        return patterns

    def extra_urls(self):
        return []

class StarkSite(object):
    def __init__(self):
        self._registry = []
        self.app_name = 'stark'
        self.namespace = 'stark'

    def register(self,model_class,handler_class=None,prev=None):
        """
        model_class: models 中的数据库相关的类
        """
        if not handler_class:
            handler_class = StarkHandler
        self._registry.append({'model_class': model_class,"handler": handler_class(model_class,prev),"prev": prev})
        """
        self._registry = 
        [
           {'model_class': models.Depart,'handler': DepartHandler(models.Depart)},
           {'model_class': models.UserInfo,'handler': UserInfoHandler(models.UserInfo)},
           {'model_class': models.Host,'handler': HostHandler(models.Host)}
        ]
        """

    def get_urls(self):
        patterns = []
        for item in self._registry:
            model_class = item['model_class']
            handler = item['handler']
            prev = item['prev']
            if prev:
                app_label,model_name = model_class._meta.app_label,model_class._meta.model_name
                # patterns.append(url(r'%s/%s/%s/list/$' %(prev,app_label,model_name),handler.changelist_view ))
                # patterns.append(url(r'%s/%s/%s/add/$' % (prev,app_label, model_name), handler.add_view))
                # patterns.append(url(r'%s/%s/%s/edit/(\d+)/$' % (prev,app_label, model_name), handler.change_view))
                # patterns.append(url(r'%s/%s/%s/del/(\d+)/$' % (prev,app_label, model_name), handler.delete_view))
                patterns.append(url(r'^%s/%s/%s/' %(prev,app_label,model_name),(handler.get_urls(),None,None)))
            else:
                app_label, model_name = model_class._meta.app_label, model_class._meta.model_name
                # patterns.append(url(r'%s/%s/list/$' % (app_label, model_name), handler.changelist_view))
                # patterns.append(url(r'%s/%s/add/$' % (app_label, model_name), handler.add_view))
                # patterns.append(url(r'%s/%s/edit/(\d+)/$' % (app_label, model_name), handler.change_view))
                # patterns.append(url(r'%s/%s/del/(\d+)/$' % (app_label, model_name), handler.delete_view))
                patterns.append(url(r'^%s/%s/' % (app_label, model_name), (handler.get_urls(),None,None)))


        # patterns.append(url(r'x1/', lambda request: HttpResponse("X1")))
        # patterns.append(url(r'x2/', lambda request: HttpResponse("X2")))

        return patterns

    @property
    def urls(self):
        return self.get_urls(),self.app_name,self.namespace

site = StarkSite()