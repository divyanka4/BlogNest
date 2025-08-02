from django.contrib import admin

# Register your models here.
from .models import Post
from .models import ContactMessage

admin.site.register(Post)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'subject', 'submitted_at')
    readonly_fields = ('first_name', 'last_name', 'email', 'subject', 'message', 'submitted_at')
