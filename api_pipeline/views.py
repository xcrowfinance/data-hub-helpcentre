from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from .serializers import UserInlineFeedbackSurveySerializer

class UserInlineFeedbackSurveyViewSet(viewsets.ModelViewSet):
    """
    API endpoint to list user satisfaction survey results for ingestion by data flow
    """

    queryset = UserInlineFeedbackSurvey.objects.all()
    serializer_class = UserInlineFeedbackSurveySerializer
    pagination_class = PageNumberPagination