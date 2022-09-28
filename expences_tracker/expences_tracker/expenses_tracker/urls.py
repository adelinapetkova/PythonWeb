from django.urls import path

from expences_tracker.expenses_tracker.views import show_home, show_profile, edit_profile, delete_profile, edit_expense, \
    delete_expense, create_expense, create_profile

urlpatterns=(
    path('', show_home, name='index'),
    path('create/', create_expense, name='create expense'),
    path('edit/<int:pk>/', edit_expense, name='edit expense'),
    path('delete/<int:pk>/', delete_expense, name='delete expense'),
    path('profile/', show_profile, name='show profile'),
    path('profile/create/', create_profile, name='create profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
)