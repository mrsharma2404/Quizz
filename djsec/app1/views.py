from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from app1.form import *
from app1.models import *
from django.contrib import messages
from django.forms import formset_factory
from django.shortcuts import redirect
from itertools import islice 
import pymysql as mysql

# Create your views here.
def homepage(request):
    return render(request, 'index.html')


#for data show in user 
def upshow0(request,stream):
    request.session['stream1'] = stream   
    data1 = quizmodel2.objects.filter(level=1, stream=stream)
    data2 = quizmodel2.objects.filter(level=2, stream=stream)
    data3 = quizmodel2.objects.filter(level=3, stream=stream)
    return render(request, 'userchoice.html',{'data1':data1,'data2':data2,'data3':data3})

def upshow1(request,quiz_name): 
    if request.session.has_key('stream1'):
        stream = request.session['stream1']
    request.session['quiz_name1'] = quiz_name  
    all_objects= quizmodel2.objects.filter(stream=stream, quiz_name=quiz_name)
    return render(request, 'userquiz1.html', {'data':all_objects})
    
def quizcalc(request):
    o1 = request.POST.get('ao1')
    a1 = request.POST.get('a1')
    o2 = request.POST.get('ao2')
    a2 = request.POST.get('a2')
    o3 = request.POST.get('ao3')
    a3 = request.POST.get('a3')
    o4 = request.POST.get('ao4')
    a4 = request.POST.get('a4')
    o5 = request.POST.get('ao5')
    a5 = request.POST.get('a5')
    o6 = request.POST.get('ao6')
    a6 = request.POST.get('a6')
    o7 = request.POST.get('ao7')
    a7 = request.POST.get('a7')
    o8 = request.POST.get('ao8')
    a8 = request.POST.get('a8')
    o9 = request.POST.get('ao9')
    a9 = request.POST.get('a9')
    o10 = request.POST.get('ao10')
    a10 = request.POST.get('a10')
    if(o1==a1):
        c1=1
    else:
        c1=0
    if(o2==a2):
        c2=1
    else:
        c2=0
    if(o3==a3):
        c3=1
    else:
        c3=0
    if(o4==a4):
        c4=1
    else:
        c4=0
    if(o5==a5):
        c5=1
    else:
        c5=0
    if(o6==a6):
        c6=1
    else:
        c6=0
    if(o7==a7):
        c7=1
    else:
        c7=0
    if(o8==a8):
        c8=1
    else:
        c8=0
    if(o9==a9):
        c9=1
    else:
        c9=0
    if(o10==a10):
        c10=1
    else:
        c10=0
    cc= (c1+c2+c3+c4+c5+c6+c7+c8+c9+c10)
    if(cc>9):
        rem = 'Excellent'
    if(cc>6):
        rem = 'Good'
    if(cc<3):
        rem = 'Keep Trying'
    else:
        rem = 'Nice' 
    #now for quizdetail
    if request.session.has_key('stream1'):
        stream = request.session['stream1']
    if request.session.has_key('quiz_name1'):
        quiz_name = request.session['quiz_name1']
    all_objects= quizmodel2.objects.filter(stream=stream, quiz_name=quiz_name)
    if(request.session.has_key('stream1')):
        del request.session['stream1']
    if(request.session.has_key('quiz_name1')):
        del request.session['quiz_name1']
    return render(request,'quizres.html' ,{'data':all_objects, 'rem':rem, 'cc':cc, 'o1':o1, 'a1':a1, 'o2':o2, 'a2':a2, 'o3':o3, 'a3':a3, 'o4':o4, 'a4':a4, 'o5':o5, 'a5':a5, 'o6':o6, 'a6':a6, 'o7':o7, 'a7':a7 ,'o8':o8, 'a8':a8, 'o9':o9 , 'a9':a9, 'o10': o10, 'a10': a10})
    

#adminSection
def alogged(request):
    u = alogin(request.POST)
    if request.method == "POST":
        q = request.POST['user']
        p = request.POST['pwd']
        all_objects = faculty.objects.filter(username=q,password=p)
        if(all_objects):
            return HttpResponseRedirect('/achoice/')  
        else:
            return HttpResponse("Incorect password")
    else:
        return render(request,'facultylogin.html',{'form':u})

def achoice1(request):
    if request.method == "POST":      
        stream = request.POST.get('s1')
        request.session['stream'] = stream
        fac_name = request.POST.get('fac_name')
        request.session['fac_name'] = fac_name
        quiz_name = request.POST.get('quiz_name')
        request.session['quiz_name'] = quiz_name
        level = request.POST.get('s2') 
        request.session['level'] = level
        return HttpResponseRedirect('/makequiz1/')       
    else:
        obj = quizcatogery.objects.all()
        return render(request,'facultychoice.html',{'obj':obj})

def aquiz(request):
    if request.method == "POST":
        if request.session.has_key('stream'):
            stream = request.session['stream']
        if request.session.has_key('fac_name'):
            fac_name = request.session['fac_name']
        if request.session.has_key('quiz_name'):
            quiz_name = request.session['quiz_name']
        if request.session.has_key('level'):
            level = request.session['level']       
        question1 = request.POST.get('q1')
        option11 = request.POST.get('o11')
        option12 = request.POST.get('o12')
        option13 = request.POST.get('o13')
        option14 = request.POST.get('o14')
        option15 = request.POST.get('o15')
        question2 = request.POST.get('q2')
        option21 = request.POST.get('o21')
        option22 = request.POST.get('o22')
        option23 = request.POST.get('o23')
        option24 = request.POST.get('o24')
        option25 = request.POST.get('o25')
        question3 = request.POST.get('q3')
        option31 = request.POST.get('o31')
        option32 = request.POST.get('o32')
        option33 = request.POST.get('o33')
        option34 = request.POST.get('o34')
        option35 = request.POST.get('o35')
        question4 = request.POST.get('q4')
        option41 = request.POST.get('o41')
        option42 = request.POST.get('o42')
        option43 = request.POST.get('o43')
        option44 = request.POST.get('o44')
        option45 = request.POST.get('o45')
        question5 = request.POST.get('q5')
        option51 = request.POST.get('o51')
        option52 = request.POST.get('o52')
        option53 = request.POST.get('o53')
        option54 = request.POST.get('o54')
        option55 = request.POST.get('o55')
        question6 = request.POST.get('q6')
        option61 = request.POST.get('o61')
        option62 = request.POST.get('o62')
        option63 = request.POST.get('o63')
        option64 = request.POST.get('o64')
        option65 = request.POST.get('o65')
        question7 = request.POST.get('q7')
        option71 = request.POST.get('o71')
        option72 = request.POST.get('o72')
        option73 = request.POST.get('o73')
        option74 = request.POST.get('o74')
        option75 = request.POST.get('o75')
        question8 = request.POST.get('q8')
        option81 = request.POST.get('o81')
        option82 = request.POST.get('o82')
        option83 = request.POST.get('o83')
        option84 = request.POST.get('o84')
        option85 = request.POST.get('o85')
        question9 = request.POST.get('q9')
        option91 = request.POST.get('o91')
        option92 = request.POST.get('o92')
        option93 = request.POST.get('o93')
        option94 = request.POST.get('o94')
        option95 = request.POST.get('o95')
        question10 = request.POST.get('q10')
        option101 = request.POST.get('o101')
        option102 = request.POST.get('o102')
        option103 = request.POST.get('o103')
        option104 = request.POST.get('o104')
        option105 = request.POST.get('o105')
        quiz = quizmodel2.objects.create(stream=stream, level=level, fac_name=fac_name, quiz_name=quiz_name, q1=question1, a11=option11, a12=option12, a13=option13, a14=option14, ans1=option15, q2=question2, a21=option21, a22=option22, a23=option23, a24=option24, ans2=option25, q3=question3, a31=option31, a32=option32, a33=option33, a34=option34, ans3=option35, q4=question4, a41=option41, a42=option42, a43=option43, a44=option44, ans4=option45, q5=question5, a51=option51, a52=option52, a53=option53, a54=option54, ans5=option55, q6=question6, a61=option61, a62=option62, a63=option63, a64=option64, ans6=option65, q7=question7, a71=option71, a72=option72, a73=option73, a74=option74, ans7=option75, q8=question8, a81=option81, a82=option82, a83=option83, a84=option84, ans8=option85, q9=question9, a91=option91, a92=option92, a93=option93, a94=option94, ans9=option95, q10=question10, a101=option101, a102=option102, a103=option103, a104=option104, ans10=option105 )
        quiz.save()
        if(request.session.has_key('stream')):
            del request.session['stream']
        if(request.session.has_key('level')):
            del request.session['level']
        if(request.session.has_key('fac_name')):
            del request.session['fac_name'] 
        if(request.session.has_key('quiz_name')):
            del request.session['quiz_name']    
        return HttpResponse("okay saved")
    else:
        return render(request,'facultyquiz.html')


