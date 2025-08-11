from django.contrib import admin
from tasks.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "completed", "priority", "due_date", "created_at")
    list_filter = ("completed", "priority")
    search_fields = ("title", "description", "owner__username")
