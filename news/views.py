from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .filetrs import PostFilter
from .forms import PostForm
from .models import Post


class NewsList(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'
    ordering = '-time_in'
    paginate_by = 10


    def get_context_data(self,  **kwargs):
        context= super().get_context_data(**kwargs)
        context['is_not_authors']= not self.request.user.groups.filter(name='authors').exists()
        return context


class NewsDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'


class NewSearch(ListView):
    model = Post
    ordering = '-date_in'
    template_name = 'post_search.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET,queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

class NewsCreate( PermissionRequiredMixin, CreateView):
    permission_required='news.add_post'
    form_class = PostForm
    model = Post
    template_name = 'new_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        if self.request.path == 'news/article/create/':
        post.article.news="AR"
        post.save()
        return super().form_valid(form)



 class NewsUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'new_edit.html'

class NewsDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Post
    template_name = 'new_delete.html'
    context_object_name = 'posts'
    success_url = '/news/'

def author_now(request):
   user = request.user
   author_group = Group.objects.get(name='authors')
   posts= Post.objects.filter(author=user).order_by('')
   if not user.groups.filter(name='authors').exists():
       user.groups.add(author_group)
   return redirect('post_list')