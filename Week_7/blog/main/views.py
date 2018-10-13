from django.shortcuts import render,redirect,get_object_or_404
from .models import Post,Comment
from .forms import PostForm,CommentForm,UpdateCommentForm,UpdatePostForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

def post_detail(request):
    post = Post.objects.all()
    context = {
        'posts': post,
    }
    return render(request,'post.html',context)

def comments(request,id):
    post = Post.objects.get(pk = id)
    context = {
       'comments': post.comments.all()
    }
    return render(request,'comments.html',context)

def home(request):
    return render(request,'home.html')

@login_required
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post')
    else:
        form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'add_post.html', context)

@login_required
def delete_post(request, id):
    post = Post.objects.exclude(pk= id)
    context = {
        'posts': post
    }
    return render(request,'post.html',context)

@login_required
def update_post(request, id):
    instance = get_object_or_404(Post,pk=id)
    form = UpdatePostForm(request.POST or None,instance = instance)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('post')
    else:
        form = UpdatePostForm()
    context = {
        'form': form,
        'post': Post.objects.get(pk=id)
    }
    return render(request, 'update_post.html', context)

def add_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post')
    else:
        form = CommentForm()
    context = {
        'form': form
    }
    return render(request, 'comments.html', context)

@login_required
def delete_comment(request, fk, id):
    comment = Comment.objects.exclude(pk= id)
    return render(request,'comments',{'comments': comment})


@login_required
def update_comment(request, fk, id):
    instance = get_object_or_404(Comment, pk=id)
    form = UpdateCommentForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('comments')
    else:
        form = UpdateCommentForm()
    context = {
        'form': form,
        'post': Post.objects.get(pk=id)
    }
    return render(request, 'update_comments.html', context)
