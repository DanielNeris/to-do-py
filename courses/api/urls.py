from django.urls import path
from .views import CourseAPIview, ReviewAPIView

urlpatterns = [
    path('courses/', CourseAPIview.as_view(), name='courses'),
    path('reviews/', ReviewAPIview.as_view(), name='reviews')
]
