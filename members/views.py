from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate
from .forms import SignUpForm


def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  logged_in = request.user.is_authenticated
  return render(request, 'main.html', {'logged_in': logged_in})
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # 로그인 성공 시, 세션에 로그인 정보를 저장합니다.
            auth_login(request, form.get_user())
            # 홈 화면으로 리디렉션합니다.
            return redirect(reverse('main'))
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
   
   
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            
            messages.success(request, '회원가입이 완료되었습니다.')
            return redirect(reverse('login'))
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})







