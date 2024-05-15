from django.contrib import admin

from reservations.models import ReservationModel


@admin.register(ReservationModel)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'phone_number', 'created_at']
    search_fields = ['full_name', 'email', 'message']
    list_filter = ['created_at', 'updated_at']
