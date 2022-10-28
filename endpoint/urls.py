from django.urls import path
from endpoint.views import *

urlpatterns = [
    # student endpoints
    path('student/', studentView.as_view()),
    path('student/<int:id>', studentViewID.as_view()),
    # parent endpoints
    path('parent/', parentView.as_view()),
    path('parent/<int:id>', parentViewID.as_view()),
    # subject endpoints
    path('subject/', subjectView.as_view()),
    path('subject/<int:id>', subjectViewID.as_view())
]