from django.shortcuts import render,redirect
from django.views import View
from .models import Category,Product

from django.db.models import Q

from django.core.paginator import Paginator 

class ProductView(View):

    def get(self, request, *args, **kwargs):
        
        if "search" in request.GET:

            if request.GET["search"] == "" or request.GET["search"].isspace():
                return redirect("shopping:index")

            search      = request.GET["search"].replace("　"," ")
            search_list = search.split(" ")

            query       = Q()
            for word in search_list:
                query &= Q(name__contains=word)

            #.order_byメソッドで並び替えしないと、paginatorでWARNINGが出る。
            data        = Product.objects.filter(query).order_by("id")
        else:
            data    = Product.objects.all().order_by("id")


        #===========ここからページネーション処理================
        paginator   = Paginator(data,4)

        if "page" in request.GET:
            data    = paginator.get_page(request.GET["page"])
        else:
            data        = paginator.get_page(1)

        context = { "data":data }

        return render(request,"shopping/index.html",context)

    def post(self, request, *args, **kwargs):
        
        return redirect("shopping:index")
   
index   = ProductView.as_view()
