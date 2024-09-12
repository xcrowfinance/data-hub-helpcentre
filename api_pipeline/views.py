from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from .serializers import UserInlineFeedbackSurveySerializer
from inline_feedback.models import UserInlineFeedbackSurvey


class UserInlineFeedbackSurveyViewSet(viewsets.ModelViewSet):
    """
    API endpoint to capture user inline feedback survey for ingestion by data flow
    """

    queryset = UserInlineFeedbackSurvey.objects.all()
    serializer_class = UserInlineFeedbackSurveySerializer
    pagination_class = PageNumberPagination
