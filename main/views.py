from django.shortcuts import render
from django.views.generic import ListView
from core.models import Post


def index(request):
    return render(request, 'main/index.html', locals())


class PublishedPostsView(ListView):

    context_object_name = 'published_posts_list'
    queryset = Post.objects.filter(is_published=True)
    template_name = '/posts/list.html'
