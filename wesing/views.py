from django.shortcuts import render

def index(request):
    """
    홈화면 로드
    """
    return render(request, 'index.html')