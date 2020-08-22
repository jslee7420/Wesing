from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from common.forms import UserForm
from accounts.models import User


def signup1(request):
    """
    회원가입 첫번째 단계(약관동의)
    """
    if request.method=="POST":
        return redirect('common:signup2')
    return render(request, 'common/signup1.html')


def signup2(request):
    """
    계정생성
    """
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('common:signup3')
    else:
        form = UserForm()
    return render(request, 'common/signup2.html', {'form': form})




def signup3(request):
    """
    회원가입 첫번째 단계(회원가입완료)
    """
    return render(request, 'common/signup3.html')


def find_id(request):
    """
    아이디 찾기
    """
    return render(request, 'common/find_id.html')

def find_password(request):
    """
    비밀번호 찾기
    """
    return render(request, 'common/find_password.html')
