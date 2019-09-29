from django.shortcuts import render, get_object_or_404,HttpResponse,HttpResponseRedirect
from .models import *
from django.core.paginator import Paginator
# Create your views here.
def courses_page(request):
    df=courses.objects.all()
    paginator = Paginator(df, 2)

    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request,'cousre/courses.html',{'posts':posts})


def courses_detail(request,slug):
    df1=get_object_or_404(courses,slug=slug)
    #print(df1.pk)
    a=[]
    a.append(df1.video)
    df2=comment.objects.filter(comment_on=df1.pk)
    df3=len(df2)
    
    #print(len(df2))
    if request.method == 'POST':
        name=request.POST['name']
        mes=request.POST['message']

        comment.objects.create(comment_on=df1,comment_from=request.user,comments=mes)
        return HttpResponseRedirect('/course/{}'.format(slug))
    return render(request,'cousre/course-details.html',{'df1':df1,'a':a,'df2':df2,'df3':df3})