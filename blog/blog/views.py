from django.shortcuts import render
from .decorators import cache
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def index(request):
    if request.method == 'POST':
        print('POST REQUEST')
        num = int(request.POST.get('num'))
        print('Num asked >>>> ' + str(num))
        fibb_num = fibb(num)
        return render(request,'blog/index.html', {'number': fibb_num})
    else:
       return render(request,'blog/index.html', {})

@cache('sql')
def fibb(num):
    if num in (0,1):
        return num
    else:
        return fibb(num -1) + fibb(num - 2)
