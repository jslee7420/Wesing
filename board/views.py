from django.shortcuts import render,get_object_or_404,redirect
from . models import Post
from django.utils import timezone
from .forms import PostForm
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.
def post_list(request):
    """
        커뮤니티, 게시글 및 공지글 목록 출력
    """
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어

    # 조회
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-is_notice','-published_date')
    if kw:
        posts = posts.filter(
            Q(title__icontains=kw)
        ).distinct()

    
    #페이징처리
    paginator = Paginator(posts,10)
    page_obj = paginator.get_page(page)
    context = {'posts':page_obj, 'page': page, 'kw': kw}
    return render(request, 'board/post_list.html',context)
    
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    #조회수 증가시키기
    post.view+=1
    post.save()
    return render(request,'board/post_detail.html',{'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()

            return redirect('board:post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'board/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('board:post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'board/post_edit.html', {'form': form})