from django.urls import path , include
from rest_framework.routers import DefaultRouter
from .views import userModelView,singleUserModelView
from .views import categoryOP

router = DefaultRouter()
#router.register(r'signin',signupViews.userSignIn)

urlpatterns = [
      #path('',include(router.urls)),
      path('getusers/',userModelView.as_view(),name='get_users'),
      path('getuser/<int:pk>/',singleUserModelView.as_view(),name='get_user'),
      path('category/',categoryOP.as_view(),name='category_operations')
]
