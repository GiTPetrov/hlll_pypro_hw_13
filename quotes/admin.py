from django.contrib import admin

from quotes.models import Quote, QuoteAuthor


class QuoteInline(admin.TabularInline):
    model = Quote
    extra = 5


class QuoteAdmin(admin.ModelAdmin):
    list_display = ('quote_text',)
    search_fields = ['quote_text']


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'author_birthdate', 'author_birthplace', 'author_description')
    fieldsets = [
        ('Author information', {'fields': ['author_birthdate', 'author_birthplace']}),
        ('Other information', {'fields': ['author_description']}),
    ]
    list_filter = ['author_birthdate']
    search_fields = ['author_name']
    inlines = [QuoteInline]


admin.site.register(Quote, QuoteAdmin)
admin.site.register(QuoteAuthor, AuthorAdmin)
