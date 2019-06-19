from django.shortcuts import render, redirect
from .models import TODO
# Create your views here.


def home(request):
    # global lst
    result=TODO.objects.all()

    if request.method == 'POST':
        content = request.POST.get('待办事项')
        if not content or content.strip() == '':
            return render(request, 'tu/home.html', {'清单': result, '警告': '请输入内容'})
        else:
            TODO.objects.create(thing=content, done=False)
            result = TODO.objects.all()
            return render(request, 'tu/home.html', {'清单': result})
    else:
        result = TODO.objects.all()
        print(result)
        return render(request, 'tu/home.html', {'清单': result})


def edit(request, forloop_counter):
    if request.method == 'POST':
        content = request.POST['已修改事项']
        if not content or content.strip() == '':
            return render(request, 'tu/edit.html', {'警告': '请输入内容'})
        else:
            a=TODO.objects.get(pk=forloop_counter)
            a.thing = content
            a.save()
            return redirect('tu:主页')
    else:
        content = TODO.objects.get(pk=forloop_counter).thing
        return render(request, 'tu/edit.html', {'待修改事项': content})


def about(request):
    return render(request, 'tu/about.html')


def delete(request, forloop_counter):
    if request.method == 'POST':
        TODO.objects.get(pk=int(forloop_counter)).delete()
        return redirect('tu:主页')
    else:
        return redirect('tu:主页')
