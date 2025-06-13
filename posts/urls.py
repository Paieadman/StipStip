from django.urls import path
from . import views
from .views import RegistrationAPIView, LoginAPIView

app_name='posts'

urlpatterns = [
    path('', views.post_list, name="new-post"),
    path('new-post/', views.post_new, name="new-post"),
    path('question', views.get_question),
    path('registration/', RegistrationAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),

]
