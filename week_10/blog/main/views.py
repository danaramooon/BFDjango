from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts  import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    DeleteView,
    UpdateView,
    DetailView,
    TemplateView
)
from .models import Post, Comment

class PostListView(LoginRequiredMixin,ListView):
    model = Post
    context_object_name = 'posts'


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    context_object_name = 'post'
    lookup_field = 'post_pk'

    def get_object(self):
        return Post.objects.get(id=self.kwargs[self.lookup_field])

class MyPostListView(LoginRequiredMixin,ListView):
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.my_post.for_user(self.request.user)

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields=('title','text')
    success_url=reverse_lazy('post')

    def form_valid(self,form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ('text', )
    success_url = reverse_lazy('post')

    def form_valid(self, form):
        post = Post.objects.get(id=self.kwargs['pk'])
        form.instance.post = post
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UpdateView):
    model = Post
    fields = ('text',)
    success_url = reverse_lazy('post')

    def get_queryset(self):
        return Post.my_post.for_user(user = self.request.user)

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('post')

    def get_queryset(self):
        return Post.my_post.for_user(user = self.request.user)

class CommentUpdateView(LoginRequiredMixin,UpdateView):
    model = Comment
    fields = ('text',)
    success_url = reverse_lazy('post')

class CommentDeleteView(LoginRequiredMixin,DeleteView):
    model = Comment
    success_url = reverse_lazy('post')

class HomeView(TemplateView):
   template_name =  "home.html"