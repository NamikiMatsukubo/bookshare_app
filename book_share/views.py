from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Follow
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .forms import PostForm, UserReistrationForm
from django.contrib import messages
from django.views import View
from django.contrib.auth.views import LogoutView



# タイムライン         
@login_required
def timeline(request):
    following_users = Follow.objects.filter(follower=request.user).values_list('following', flat=True)
    posts = Post.objects.filter(user__in=list(following_users) + [request.user]).order_by('-created_at')
    return render(request, 'book_share/timeline.html', {'posts': posts})

#　投稿作成
@login_required
def post_creat(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('timeline')
    else:
        form = PostForm()
    return render(request, 'book_share/post_creat.html', {'form': form})

# 投稿削除
@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.user == request.user:
        if request.method == 'POST':
            post.delete()
            return redirect('timeline')
        return render(request, 'book_share/post_delete.html', {'post': post})
    else:
        return redirect('book_share/timeline')

# ユーザーページ
def user_page(request, username):
    user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(user=user).order_by('-created_at')
    return render(request, 'book_share/user_page.html', {'user': user, 'posts': posts} )

# ユーザー認証
def register(request):
    if request.method == 'POST':
        form = UserReistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            login(request, user)
            messages.success(request, 'ユーザー登録が完了しました。')
            return redirect("/")
    else:
        form = UserReistrationForm()
    return render(request,'book_share/register.html', {'form': form})   
    
# ログイン機能
def user_login(request):
    if request.method == 'POST':
        username = request.POST['useername']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.error(request, 'ユーザー名またはパスワードが間違っています。')
            return render(request, 'book_share/login.html')
        else:
            return redirect('/')
    return redirect('/')

# # ログアウト機能
# def logout(request):
#     logout(request)
#     return redirect('login')

# ログアウト機能
class CustomLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
        return redirect('login')

# フォロー機能 
def follow_user(request, username):
    if request.user.is_authenticated: # ログインしている場合のみフォロー可能
        user_to_follow = get_object_or_404(User, username=username)
        if request.user != user_to_follow: # 自分自身はフォローできない
            Follow.objects.get_or_create(follower=request.user, following=user_to_follow)
    return redirect('user_page', username=username) # ユーザーページにリダイレクト

# フォロー解除   
def unfollow_user(request, username):
    if request.user.is_authenticated:
        user_to_unfollow = get_object_or_404(User, username=username)
        Follow.objects.filter(follower=request.user, following=user_to_unfollow).delete()
    return redirect('user_page', username=username) # ユーターページにリダイレクト

#　投稿一覧
# def post_list(request):
#     posts = Post.objects.all().order_by('-created_at')
#     return render(request, 'book_share/post_list.html', {'posts': posts})