from django.shortcuts import render,redirect
from .models import Post,Comment
from .forms import PostForm,CommentForm,UpdateCommentForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

def post_detail(request):
    post = Post.objects.all()
    context = {
        'post': post
    }
    return render(request,'post.html',context)

def comment(request,id):
    post = Post.objects.get(pk = id)
    context = {
       'post':post
    }
    return render(request,'post.html',context)

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
def delete_post(request, pk):
    post = Post.objects.get(pk= pk).exclude()
    return render(request,'post.html')

@login_required
def update_post(request, pk):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = Post.objects.get(pk=pk)
            post.title = form.cleaned_data['title']
            post.content = form.cleaned_data['content']
            post.save()
            return render(request,'post.html')
    else:
        form = PostForm()
    context = {
        'form': form,
        'post': Post.objects.get(pk=pk)
    }
    return render(request, 'update_post.html', context)

@login_required
def delete_comment(request, fk, pk):
    comment = Comment.objects.get(pk= pk)
    comment.delete()
    return redirect('..')

@login_required
def update_comment(request, fk, pk):
    if request.method == 'POST':
        form = UpdateCommentForm(request.POST)
        if form.is_valid():
            comment = Comment.objects.get(pk=pk)
            comment.comment = form.cleaned_data['comment']
            comment.save()
            return redirect('..')
    else:
        form = UpdateCommentForm()
    context = {
        'form': form,
        'comment': Comment.objects.get(pk=pk)
    }
    return render(request, 'update_comment.html', context)

