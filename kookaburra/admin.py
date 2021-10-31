from django.contrib import admin

# Register your models here.
from .models import KookaburraPost, KookaburraComment, KookaburraSection


class PostAdmin(admin.ModelAdmin):
    pass


class SectionAdmin(admin.ModelAdmin):
    pass


class CommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(KookaburraPost, PostAdmin)
admin.site.register(KookaburraComment, CommentAdmin)
admin.site.register(KookaburraSection, SectionAdmin)
