from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from Myblog.models import Category, Page
# Create your views here.

def index(request):

    category_list = Category.objects.order_by('name')[:5]
    context_dict = {'categories' : category_list}

    return render(request,'main.html', context_dict)

def category(request, category_name_slug):

    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name

        pages = Page.objects.filter(category=category)

        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        pass

    return render(request, 'diary.html', context_dict)