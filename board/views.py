from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
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
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by(
        '-is_notice', '-published_date')
    if kw:
        posts = posts.filter(
            Q(title__icontains=kw)  # 제목 검색
        ).distinct()

    # 페이징처리
    paginator = Paginator(posts, 10)
    page_obj = paginator.get_page(page)
    context = {'posts': page_obj, 'page': page, 'kw': kw,
               'navbar_title': '커뮤니티', 'navbar_subtitle': '커뮤니티에서 다양한 정보와 공지사항을 받아 보세요.', 'navbar_background': 'background: linear-gradient(90deg, rgba(255,113,134,1) 0%, rgba(201,201,255,1) 0%, rgba(199,234,222,1) 100%);'}
    return render(request, 'board/post_list.html', context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # 조회수 증가시키기
    post.view += 1
    post.save()
    return render(request, 'board/post_detail.html', {'post': post, 'navbar_background': 'background: linear-gradient(90deg, rgba(255,113,134,1) 0%, rgba(201,201,255,1) 0%, rgba(199,234,222,1) 100%);'})


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
    return render(request, 'board/post_edit.html', {'form': form, 'navbar_background': 'background: linear-gradient(90deg, rgba(255,113,134,1) 0%, rgba(201,201,255,1) 0%, rgba(199,234,222,1) 100%);'})


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
    return render(request, 'board/post_edit.html', {'form': form, 'navbar_background': 'background: linear-gradient(90deg, rgba(255,113,134,1) 0%, rgba(201,201,255,1) 0%, rgba(199,234,222,1) 100%);'})


def answer_create(request, post_id):
    """
    답변등록
    """
    post = get_object_or_404(Post, pk=post_id)
    post.answer_set.create(content=request.POST.get(
        'content'), created_date=timezone.now(), author=request.user)
    return redirect('board:post_detail', pk=post.id)
