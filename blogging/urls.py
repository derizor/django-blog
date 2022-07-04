from django.urls import path
from blogging.views import BlogListView, BlogDetailView
# from blogging.views import list_view
# from blogging.views import BlogListView
# from blogging.views import detail_view

urlpatterns = [
    path('', BlogListView.as_view(), name="blog_index"),
    # path('posts/<int:post_id>/', stub_view, name="blog_detail"),]
    path('posts/<int:pk>/', BlogDetailView.as_view(), name="blog_detail"),]

