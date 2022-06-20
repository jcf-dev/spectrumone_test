from django.urls import path, include
from dj_rest_auth.registration.views import VerifyEmailView, ConfirmEmailView

urlpatterns = [
    path("auth/", include("dj_rest_auth.urls")),
    path(
        "auth/register/account-confirm-email/<str:key>/",
        ConfirmEmailView.as_view(),
    ),
    path("auth/register/", include("dj_rest_auth.registration.urls")),
    path(
        "auth/register/account-confirm-email/",
        VerifyEmailView.as_view(),
        name="account_email_verification_sent",
    ),
]
