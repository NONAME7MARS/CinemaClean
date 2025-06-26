from django.contrib import admin
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Movie, Hall, Session, Ticket, Dashboard, Review
from .forms import SessionForm
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


# 🎬 Фільми
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_year', 'genre', 'duration', 'rating', 'director')
    search_fields = ('title', 'genre', 'director')
    list_filter = ('genre', 'release_year')
    ordering = ('-release_year',)
    fieldsets = (
        (None, {'fields': ('title', 'description', 'poster')}),
        ('Інформація', {'fields': ('genre', 'duration', 'rating', 'release_year', 'director')}),
    )
    readonly_fields = ('rating',)
    list_per_page = 20

# 🏛️ Зали
@admin.register(Hall)
class HallAdmin(admin.ModelAdmin):
    list_display = ('number', 'capacity', 'type')
    list_filter = ('type',)
    ordering = ('number',)

# 📅 Сеанси
@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    form = SessionForm
    list_display = ('movie', 'hall', 'date', 'start_time', 'end_time')
    list_filter = ('date', 'movie', 'hall__type')
    search_fields = ('movie__title', 'hall__number')
    date_hierarchy = 'date'
    ordering = ('-date', 'start_time')

# 🎟️ Квитки
@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('session', 'seat_number', 'price', 'status')
    list_filter = ('status', 'session__movie', 'session__date')
    search_fields = ('session__movie__title', 'seat_number')
    autocomplete_fields = ['session']
    ordering = ('-id',)
    list_per_page = 30

# 📊 Аналітика – псевдомодель
class DummyAnalyticsModel:
    _meta = type('Meta', (), {
        'app_label': 'analytics',
        'model_name': 'аналітика',
        'verbose_name_plural': '📊 Аналітика',
    })

class AnalyticsAdmin(admin.ModelAdmin):
    def changelist_view(self, request, extra_context=None):
        return HttpResponseRedirect(reverse('analytics'))

    def has_module_permission(self, request):
        return self._has_analytics_access(request)

    def has_view_permission(self, request, obj=None):
        return self._has_analytics_access(request)

    def _has_analytics_access(self, request):
        return (
            request.user.is_superuser or
            request.user.groups.filter(name__in=["Директор"]).exists()
        )

    def has_add_permission(self, request): return False
    def has_change_permission(self, request, obj=None): return False
    def has_delete_permission(self, request, obj=None): return False

admin.site.register(Dashboard, AnalyticsAdmin)


class CustomUserAdmin(UserAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if not request.user.is_superuser:
            # Заборонити бачити / змінювати флаг superuser
            if 'is_superuser' in form.base_fields:
                form.base_fields['is_superuser'].disabled = True
        return form

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('movie', 'user', 'rating', 'created_at')
    list_filter = ('rating', 'movie')
    search_fields = ('user__username', 'movie__title', 'text')
    ordering = ('-created_at',)
