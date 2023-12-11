from django.contrib import admin
from .models import Book, Category


class BookAdmin(admin.ModelAdmin):
    """
    Creates Admin For The Books
    """
    fieldsets = []

    ordering = ('sku',)
    list_display = (
        'sku',
        'ISBN',
        'author',
        'title',
        'pages',
        'this_publication_date',
        'condition',
        'language',
        'price',
        'rating',
    )
    
class CategoryAdmin(admin.ModelAdmin):
    """
    Creates Admin For The Catergorys
    """
    fieldsets = []
    list_display = (
        'view_name',
        'name',
    )

admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)
