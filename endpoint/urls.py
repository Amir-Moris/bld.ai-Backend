from django.urls import path, include
from endpoint.views import *

urlpatterns = [
    # student
    path('student/', include([
        path('', StudentView.as_view()),
        path('<int:id>', StudentViewID.as_view())
    ])),
    # subject
    path('subject/', include([
        path('', SubjectView.as_view()),
        path('<int:id>', SubjectViewID.as_view())
    ])),
    # parent
    path('parent/', include([
        path('', ParentView.as_view()),
        path('<int:id>', ParentViewID.as_view())
    ]))
]