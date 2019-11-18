from django.urls import path
from .views import ListSongsView


urlpatterns = [
    path('', ListSongsView.as_view(), name="songs-all"),
]