from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts  import render
from django.urls import reverse_lazy
from .form import PostUpdateForm
from django.views.generic import (
    ListView,
    CreateView,
    DeleteView,
    UpdateView,
    DetailView
)
from .models import Post,Comment

class PostListView(LoginRequiredMixin,ListView):
    model = Post
    context_object_name = 'Post'

class MyPostListView(LoginRequiredMixin,ListView):
    model = Post
    context_object_name = 'Post'

    def get_queryset(self):
        return Post.myPost.my_post(user=self.request.user)

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields=('title','text')
    success_url=reverse_lazy('post')

    def form_valid(self,form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class CommentDetailView(LoginRequiredMixin,ListView):
    model = Comment
    context_object_name = 'Comment'

class PostCommentCreateView(LoginRequiredMixin,CreateView):
    model = Comment
    fields=('text',)
    success_url=reverse_lazy('comment')

    def form_valid(self,form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UpdateView):
    model = Post
    form_class = PostUpdateForm
    success_url = reverse_lazy('post')

    def get_queryset(self):
        return Post.myPost.my_post(user = self.request.user)

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('post')

    def get_queryset(self):
        return Post.myPost.my_post(user = self.request.user)

class CommentUpdateView(LoginRequiredMixin,UpdateView):
    model = Comment
    form_class = PostUpdateForm
    success_url = reverse_lazy('comment')

    def get_queryset(self):
        return Comment.myPost.my_post(user = self.request.user)

class CommentDeleteView(LoginRequiredMixin,DeleteView):
    model = Comment
    success_url = reverse_lazy('comment')

    def get_queryset(self):
        return Comment.myPost.my_post(user = self.request.user)

def home(request):
    return render(request, "home.html")