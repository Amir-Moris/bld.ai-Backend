from django.urls import path
from .views import get_post
from .views import put_delete

urlpatterns = [
    path('', get_post),
    path('<int:ID>', put_delete)
]