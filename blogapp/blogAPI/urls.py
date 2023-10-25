from django.urls import path , include
from rest_framework.routers import DefaultRouter
from .views import signupViews

router = DefaultRouter()
#router.register(r'signin',signupViews.userSignIn)

urlpatterns = [
#      path('',include(router.urls)),
      path('getusers/',signupViews.userModelView.as_view(),name='get_users'),
      path('getuser/<int:pk>/',signupViews.singleUserModelView.as_view(),name='get_user')
]
