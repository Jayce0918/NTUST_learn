from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .models import User
from .form import RegisterForm, EditForm
from django.contrib.auth.forms import SetPasswordForm


def home(request):
    return render(request,'home.html')
def register(request):
    return render(request,'register.html')
def User_login(request):
    return render(request,'login.html')
def personal(request):
    return render(request,'personal.html')
def User_logout(request):
    return render(request,'home.html')
def coursestart(request):
    return render(request,'coursestart.html')
def class1(request):
    return render(request,'class1.html') 
def htmlcss(request):
    return render(request,'htmlcss.html')     

def register(request):
  if request.method == 'POST':
    form = RegisterForm(request.POST)
    if form.is_valid():
        new_user = form.save()
        # 如果希望註冊完馬上登入可加入，若無需求可不加
        # ------------------------------------
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(request, user)
        # ------------------------------------
        return HttpResponseRedirect('/')
  else:
    form = RegisterForm()
  return render(request,'register.html',{'form':form,})

# 在learning/views.py 新增 User_login
def User_login(request):
    # 如果已經登入，跳至個人頁面
    # 此階段為空白頁面
    if request.user.is_authenticated:
        return HttpResponseRedirect('/coursestart/')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        # 如果User是已註冊的就login
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/coursestart/')
        else:
            # 如果登入失敗，則丟出錯誤訊息
            error_message = "帳號不存在或是密碼錯誤，請再試一次"
            return render(request,'login.html',{'error_message':error_message})
    return render(request,'login.html')

# 在learning/views.py再加入User_logout function
def User_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

# 在 views.py 中新增 personal function
# 此為修改普通資料的 view
def personal(request):
    instance = User.objects.get(username=request.user.username)
    if request.method == 'POST':
        form = EditForm(request.POST,instance=instance)
        if form.is_valid():
            form.save()
    else:
        form = EditForm(instance=instance)
    return render(request, 'personal.html',
        {
            'account': request.user.username,
            'form':form
        })

def reset_password(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login/')
    form = SetPasswordForm(user=request.user, data=request.POST)
    if form.is_valid():
        form.save()
        #update_session_auth_hash(request, form.user)
        return HttpResponseRedirect('/logout/')
    return render(request, 'reset.html',{ 'form':form })

# 留言板


#作業牆


