from django.contrib import admin

from .models import Author, Book, Genra, BookInstance


class BookInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BookInstanceInline]



@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'last_name',
        'first_name',
        'date_of_birth',
        'date_of_death',
    )
    fields =['first_name', 'last_name', ('date_of_birth', 'date_of_death')]


admin.site.register(Genra)


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    fieldsets = (
        (
            None, {
                'fields': ('book', 'imprint', 'id')
            }
        ),
        (
            'Availability', {
                'fields': ('status', 'due_back')
            }
        ),
    )


