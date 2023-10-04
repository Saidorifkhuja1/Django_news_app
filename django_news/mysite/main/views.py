from django.shortcuts import render

def index(request):
    data = {
        'title': 'MainPage!'
    }
    return render(request, 'main/main.html',data)


def about(request):
    return render(request, 'main/about.html')