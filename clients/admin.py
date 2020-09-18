from django.contrib import admin

from .models import Client, Comment, Computer


class CommentInline(admin.TabularInline):
    model = Comment

# added for ec
class ComputerInLine(admin.TabularInline):
    model =Computer


class ClientAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline, ComputerInLine
    ]

admin.site.register(Client, ClientAdmin)
admin.site.register(Comment)
admin.site.register(Computer)