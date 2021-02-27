from django.contrib import admin
from blog_app.models import post,author,Comment

# Register your models here.
class author_admin(admin.ModelAdmin):
    list_display=["name"]

admin.site.register(author,author_admin)


class post_model_admin(admin.ModelAdmin):
    list_display=["title","content","create_time","update_time"]
    list_filter=["title","create_time"]
    search_fields=["title"]


    class Meta:
        model=post

admin.site.register(post,post_model_admin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'Post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


admin.site.register(Comment,CommentAdmin)
