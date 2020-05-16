from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from posts.forms import PostForm, CommentForm, Post, Comment
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseForbidden, HttpResponseRedirect, Http404


def index(request):
    posts = get_list_or_404(Post)
    return render(request, 'index.html', {'posts': posts})


class PostCreateView(SuccessMessageMixin, CreateView, LoginRequiredMixin):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('posts:my_list')
    template_name = 'posts/post_form.html'
    # success_message = "Post was created successfully"

    def get_success_message(self, cleaned_data):
        return self.object.title+" added successfully"

    def form_valid(self, form):
        form.instance.author = self.request.user.userprofile
        return super().form_valid(form)


class PostUpdateView(SuccessMessageMixin, UpdateView, LoginRequiredMixin):
    model = Post
    form_class = PostForm

    def get_success_url(self):
        return reverse_lazy('posts:detail', kwargs={'slug': self.object.slug})

    def get_success_message(self, cleaned_data):
        return self.object.title+' updated successfully'


class PostDeleteView(DeleteView, LoginRequiredMixin):
    model = Post
    context_object_name = 'post'
    success_url = reverse_lazy('posts:my_list')


class MyPostListView(ListView):
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user.userprofile)


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    extra_context = {'comment_form': CommentForm}


# ClassBasedView for Post-Comment system
# All functions and algorithms similar to Function Based View
# You will better understand this version if you try to implement FBV
class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm

    def get_success_url(self):
        return reverse_lazy('posts:detail', kwargs={'slug': self.object.post.slug})

    def form_valid(self, form):
        post = get_object_or_404(Post, slug=self.kwargs['slug'])
        form.instance.post = post
        form.instance.author = self.request.user.userprofile
        return super().form_valid(form)


# This post-comment implementation using FunctionBasedViews
# It's simpler but in overall similar to ClassBasedImplementation
def post_detail_view(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            form.instance.post = post
            form.instance.author = request.user.userprofile
            form.save(commit=True)
            reverse_lazy('posts:detail', kwargs={'slug': slug})

    form = CommentForm()
    return render(request, 'posts/detail.html', {'post': post, 'form': form})
