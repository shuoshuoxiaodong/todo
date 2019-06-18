from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'tu/home.html')


def edit(request):
    return render(request, 'tu/edit.html')

def about(request):
    return render(request, 'tu/about.html')
