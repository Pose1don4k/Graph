from django.contrib import admin
from .models import Graph

@admin.register(Graph)
class GraphAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at', 'color', 'thickness', 'scale')
    list_filter = ('user', 'created_at', 'color')
    search_fields = ('title', 'user__username')
