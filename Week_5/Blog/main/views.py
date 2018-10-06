from django.shortcuts import render, redirect
from .models import User,Post,Comment
from datetime import date, timedelta
from django.views.decorators.csrf import csrf_exempt
from .forms import PostForm

@csrf_exempt
def posts(request):
    posts = Post.objects.all()
    context = {
        'Post': posts
    }
    return render(request, 'posts.html', context)


@csrf_exempt
def comments(request):
    posts = Comment.objects.all()
    context = {
        'Comment': posts.comments.all()
    }
    return render(request, 'comments.html', context)

#def create(request,forms,html,add):
 #   if request.method == 'POST':
  #      form = forms(request.POST)
   #     if form.is_valid():
     #       form.save()
      #      return redirect(html)
    #else:
     #   form = forms()
      #  context = {
       #     'forms': forms
        #}
    #return render(request, add,context)
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts.html')
    else:
        form = PostForm()
        context = {
            'forms': form
        }
    return render(request, 'add_post.html',context)

