from django.shortcuts import render


def blogs(request):
    cars = [
        {'id': 1 ,'name': 'BMW M5 E60', 'color': 'black', 'year': '2010'},
        
        ]
    context = {
        'list':'Mashinalar royhati',
        'cars': cars
    }
    return render(request, 'blog.html', context)


def blog_detail(request, id):
    context = {
        'list2':'Kompaniyalar royxati'
    }
    return render(request, 'blog-detail.html', context)


def comment_create(request):
    context = {
        'list3':'Dasturlash turlari'
    }
    return render(request, 'comment.html', context)

