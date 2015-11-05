from django.contrib import admin

from .models import Menu, Сategory, Project,\
PreInform, Clients, Social, Contact, Tag, Post


class MenuTabular(admin.TabularInline):
    model = Menu
    extra = 3

class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'link')
    inlines = [MenuTabular]

admin.site.register(Menu, MenuAdmin)

admin.site.register(Сategory)
admin.site.register(Project)
admin.site.register(PreInform)
admin.site.register(Clients)
admin.site.register(Social)
admin.site.register(Contact)
admin.site.register(Tag)
admin.site.register(Post)
