from django.shortcuts import render,HttpResponse
from app01 import models
# Create your views here.
class PageInfo(object):
    def __init__(self,current_page,date_count,per_page):
        self.current_page = current_page
        self.per_page = per_page
        a,b = divmod(date_count,per_page)
        if b:
            a+=1
        self.all_page = a

    def start(self):
        return(self.current_page-1)*self.per_page

    def end(self):
        return(self.current_page*self.per_page)

    def page(self):
        page_list = []
        for i in range(1,self.all_page+1):
            temp="<a href='/?page=%s'>%s</a>"%(i,i)
            page_list.append(temp)
        return ''.join(page_list)


def index(request):
    page_info = PageInfo(int(request.GET.get('page')), models.User.objects.all().count(),10)

    user_list = models.User.objects.all()[page_info.start():page_info.end()]

    return render(request,'index.html',{'user_list':user_list,'page_info':page_info})

