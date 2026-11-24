from django.contrib import admin
from .models import WasteComplaint

admin.site.site_header = "CleanCity Administration - Hariom Mishra"
admin.site.site_title = "CleanCity Admin Portal"
admin.site.index_title = "Waste Management System Control Panel"

@admin.register(WasteComplaint)
class WasteComplaintAdmin(admin.ModelAdmin):
    list_display = ('tracking_number', 'user', 'category', 'location', 'urgency', 'status', 'created_at')
    list_filter = ('status', 'category', 'urgency', 'created_at')
    search_fields = ('location', 'landmark', 'description', 'user__username', 'user__email')
    list_editable = ('status', 'urgency')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)
    
    fieldsets = (
        ('Complaint Overview', {
            'fields': ('user', 'category', 'location', 'landmark', 'urgency', 'description', 'photo')
        }),
        ('Status & Progress Update', {
            'fields': ('status', 'admin_notes')
        }),
        ('Timestamp Metadata', {
            'fields': ('created_at', 'updated_at')
        }),
    )
