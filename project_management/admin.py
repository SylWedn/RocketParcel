from django.contrib import admin, messages

from project_management.models import Packagedb, Category


@admin.register(Packagedb)
class PackagedbAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title', 'time_create', 'is_published', 'cat', 'brief_info')
    list_display_links = ('id', 'title')
    list_editable = ('is_published', 'cat')
    list_per_page = 3
    actions = ['set_published', 'set_draft']
    search_fields = ['title',]
    list_filter = ['is_published', 'cat']
    def brief_info(self, women: Packagedb):
        return f"description {len(women.content)} symbols"

    @admin.action(description='Publish selected posts')
    def set_published(self, request, queryset):
        """Set is_published=True for selected objects."""
        count = queryset.update(is_published=Packagedb.Status.PUBLISHED)
        self.message_user(request, f'Changed {count} posts')

    @admin.action(description="Remove from publication")
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Packagedb.Status.DRAFT)
        self.message_user(request, f"{count} Removed publications", messages.WARNING)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


