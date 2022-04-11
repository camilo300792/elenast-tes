from django.urls import path
from auth.views import SignInAPIView, SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='auth_signup'),
    path('signin/', SignInAPIView.as_view(), name='auth_signin'),
]