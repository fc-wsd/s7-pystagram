from django.contrib import admin
from photos.models import Photo
from photos.models import Comment
from photos.models import Tag

class CommentInlineAdmin(admin.StackedInline):
    model = Comment
    extra = 1
 
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id','created_at',)
    list_display_links = ('id','created_at',)
    ordering = ('id','created_at',)
    inlines = (CommentInlineAdmin,)
    list_filter = ('tags',)
    search_fields = ('content',)
    date_hierarchy = 'created_at'
   
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Comment)
admin.site.register(Tag)
