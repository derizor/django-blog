from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from blogging.models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class BlogListView(ListView):

    # model = Post
    queryset = Post.objects.order_by('-id') # reverse-chronological order
    template_name = 'blogging/list.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blogging/detail.html'
    context_object_name = 'post'
    queryset = Post.objects.all()

    # def post(self, request, *args, **kwargs):
    #     post = self.get_object()

    #     # published = Post.objects.exclude(published_date__exact=None)
    #     context = {'object': post}
    #     return render(request, 'blogging/detail.html', context)

