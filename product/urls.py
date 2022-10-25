from django.urls import path 
from .views import productViewMultiple, productViewSingle

urlpatterns = [
    path('', productViewMultiple.as_view()),
    path('<int:id>', productViewSingle.as_view())
]