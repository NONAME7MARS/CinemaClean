from django.urls import path
from . import views, admin_views
from .views import admin_dashboard

urlpatterns = [
    path('', views.movie_list, name='movie_list'),  # Головна (афіша)
    path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),  # Сторінка фільма
    path('session/<int:session_id>/booking/', views.booking, name='booking'), # Бронювання
    path('booking/success/', views.booking_success, name='booking_success'),
    path('session/<int:session_id>/checkout/', views.checkout, name='checkout'),
    path('session/<int:session_id>/confirm/', views.confirm_checkout, name='confirm_checkout'),
    path('ticket/<int:ticket_id>/pdf/', views.download_ticket_pdf, name='ticket_pdf'),
    path('autocomplete_movies/', views.autocomplete_movies, name='autocomplete_movies'),
    path('analytics/', admin_views.analytics_view, name='analytics'),
    path('analytics/export/pdf/', admin_views.export_analytics_pdf, name='analytics_export_pdf'),
    path('analytics/export/excel/', admin_views.export_analytics_excel, name='analytics_export_excel'),
    path('account/', views.user_dashboard, name='user_dashboard'),
    path('account/login/', views.custom_login, name='login'),
    path('account/logout/', views.custom_logout, name='logout'),
    path('account/register/', views.register, name='register'),
    path('favorite/<int:movie_id>/toggle/', views.toggle_favorite, name='toggle_favorite'),
    path("movies/<int:movie_id>/review/update/", views.update_review, name="update_review"),
    path("movie/<int:movie_id>/review/delete/", views.delete_review, name="delete_review"),
    path("review/<int:review_id>/update-from-profile/", views.update_review_from_profile, name="update_review_from_profile"),
    path("review/<int:review_id>/delete-from-profile/", views.delete_review_from_profile, name="delete_review_from_profile"),
    path('account/use-bonus/', views.use_bonus, name='use_bonus'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('about/', views.about_view, name='about'),
    path("contacts/", views.contacts_view, name="contacts"),
    path("faq/", views.faq_view, name="faq"),

]
