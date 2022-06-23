from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField(blank=True)
    # posts = models.ManyToManyField(Post, blank=True, related_name='categories')

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)
    categorys = models.ManyToManyField(Category, related_name='categories', verbose_name="Categories")

    def __str__(self):
        return f"{self.title}, {self.author}, {self.published_date}"

# class Post(models.Model):
#     title = models.CharField(max_length=128)
#     text = models.TextField(blank=True)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     created_date = models.DateTimeField(auto_now_add=True)
#     modified_date = models.DateTimeField(auto_now=True)
#     published_date = models.DateTimeField(blank=True, null=True)
#     categorys = models.ManyToManyField(Category, related_name='categories')

#     def __str__(self):
#         return self.title

# class Category(models.Model):
#     name = models.CharField(max_length=60)
#     description = models.TextField(blank=True)
#     posts = models.ManyToManyField(Post, blank=True, related_name='categories')

#     class Meta:
#         verbose_name_plural = 'Categories'

#     # name = models.CharField(max_length=60)
#     # description = models.TextField(blank=True)
#     # posts = models.ManyToManyField(Post, blank=True, related_name='categories')

#     def __str__(self):
#         return self.name

#_______________________________________________

# categ = Category.objects.all()
# categ_tag = tuple(i.name for i in categ)

# print("THESE ARE ALL CATEGORIES:", categ_tag)

#     pass
