from django.urls import path

from notes.web.views import show_home, show_profile, show_note_details, add_note, delete_note, edit_note, \
    create_profile, delete_profile

urlpatterns=(
    path('', show_home, name='index'),
    path('add/', add_note, name='add note'),
    path('edit/<int:pk>/', edit_note, name='edit note'),
    path('delete/<int:pk>/', delete_note, name='delete note'),
    path('details/<int:pk>/', show_note_details, name='show note details'),
    path('profile/', show_profile, name='show profile'),
    path('profile/create/', create_profile, name='create profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
)

