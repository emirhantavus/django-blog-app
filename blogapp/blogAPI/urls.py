from django.urls import path , include
from rest_framework.routers import DefaultRouter
from .views import signupViews

router = DefaultRouter()
router.register(r'signin',signupViews.userSignIn)

urlpatterns = [
      path('',include(router.urls)),
]
