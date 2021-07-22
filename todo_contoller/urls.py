from django.urls import path,include
from todo_contoller import views
from rest_framework import routers
from .views import RegisterView,LoginView,UserView,LogoutView

router = routers.DefaultRouter()
router.register('studentapi',views.StudentView,basename="studentview")

urlpatterns = [
    path('',include(router.urls)),
    path('register',RegisterView.as_view()),
    path('login',LoginView.as_view()),
    path('user',UserView.as_view()),
    path('logout',LogoutView.as_view()),
]