from django.contrib import admin
from blogging.models import Post, Category
# from blogging.myapp.models import Author

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # exclude = ('published_date',)
    list_display = ("title", "author", 'published_date')
    list_filter = ("published_date",)

    # fields = ('title', 'text', 'author', 'categorys')

    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


    # exclude = ('published_date',)

    # pass

# admin.site.register(Post) # Original
# admin.site.register(Category) # Original

