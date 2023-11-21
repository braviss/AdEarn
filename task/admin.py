from django.utils import timezone
from django.contrib import admin
from task.models import (
    Task,
    Category,
)



@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status',)
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ["status", ]
    actions = ["update_order_to_now", "activate_all_task"]


    @admin.action(description="Task Up")
    def update_order_to_now(self, request, queryset):
        queryset.update(order=timezone.now())

    @admin.action(description="Activate")
    def activate_all_task(self, request, queryset):
        queryset.update(status=True)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

