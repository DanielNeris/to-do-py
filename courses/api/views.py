from rest_framework.views import APIView
from rest_framework.response import Response

from courses.models import Course, Review
from .serializers import CourseSerializer, ReviewSerializer


class CourseAPIview(APIView):
    """
    API COURSES
    """

    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)


class ReviewAPIview(APIView):
    """
    API REVIEWS
    """

    def get(self, request):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
