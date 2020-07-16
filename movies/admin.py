from django.contrib import admin
from .models import Category, Actor, Genre, Movie, MovieShots, Rating, RatingStar, Reviews
from django.utils.safestring import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget



class MovieAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget(), label='Описание')
    class Meta:
        model = Movie
        fields = '__all__'


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name','url')
    list_display_links = ('name',)


class ReviewInline(admin.TabularInline):
    model = Reviews
    extra = 1
    readonly_fields = ('email','name')


class MovieShotsInline(admin.TabularInline):
    model = MovieShots
    extra = 1
    readonly_fields = ('get_image',)
    list_display = ('name','age','get_image')


    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = 'Изображение'


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title','category','url','draft','get_image')
    readonly_fields = ('get_image',)
    list_filter = ('category','year')
    search_fields = ('title','category__name')
    inlines = [MovieShotsInline,ReviewInline]
    save_on_top = True
    save_as = True
    list_editable = ('draft',)
    actions = ['publish', 'un_publish']
    form = MovieAdminForm
    fieldsets = (
        (None, {
            'fields':(('title','tag_line'),)
        }),
        (None, {
            'fields': ('description', ('poster','get_image'))
        }),
        (None, {
            'fields': (('year', 'world_premier','country'),)
        }),
        ('Actors', {
            'classes':('collapse',),
            'fields': (('actors','genres','directors','category'),)
        }),
        (None, {
            'fields': (('budget', 'fees_in_usa','fees_in_world'),)
        }),
        ('Options', {
            'fields': (('url', 'draft'),)
        }),
    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="100" height="110"')

    get_image.short_description = 'Постер'

    def publish(self, request, queryset):
        row_update = queryset.update(draft=False)
        message_bit = f'{row_update} записей обновлено'
        self.message_user(request, f'{message_bit}')


    def un_publish(self, request, queryset):
        row_update = queryset.update(draft=True)
        message_bit = f'{row_update} записей обновлено'
        self.message_user(request, f'{message_bit}')

    publish.short_description = 'Опубликовать'
    publish.allowed_permissions = ('change',)

    un_publish.short_description = 'Снять с публикации'
    un_publish.allowed_permissions = ('change',)

@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('name','email','parent','movie','id')
    readonly_fields = ('name','email')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name','url')


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('name','age','get_image')


    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = 'Изображение'
    readonly_fields = ('get_image',)


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('star','ip',)


@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    list_display = ('title','movie','get_image')

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110"')

    get_image.short_description = 'Изображение'
    readonly_fields = ('get_image',)

admin.site.register(RatingStar)

admin.site.site_title = 'Django Movies'
admin.site.site_header = 'Django Movies'