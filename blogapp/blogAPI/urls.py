from django.urls import path , include
from rest_framework.routers import DefaultRouter
from .views import userModelView,singleUserModelView
from .views import categoryOP
from .views import postList
from .views import commentList
from . views import postView

router = DefaultRouter()
#router.register(r'signin',signupViews.userSignIn)

urlpatterns = [
      #path('',include(router.urls)),
      path('getusers/',userModelView.as_view(),name='get_users'),
      path('getuser/<int:pk>/',singleUserModelView.as_view(),name='get_user'),
      path('category/',categoryOP.as_view(),name='category_operations'),
      path('posts/',postList.as_view(),name='post_list'),
      path('comments/', commentList.as_view(), name='comment-list'),
      path('posts/<int:pk>',postView.showSinglePostList,name='single_post'),
]
