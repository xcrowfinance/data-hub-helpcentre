from django.urls import path

# pylint: disable=consider-using-from-import
from . import views as views

urlpatterns = [
    path(
        "<path:path>/user-inline-feedback-survey",
        views.UserInlineFeedbackSurveyViewSet.as_view({"get": "list"}),
        name="user-inline-feedback-survey",
    ),
]
