from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import RegistrationAPIView, LoginAPIView, GetQuestionAPIView, LogoutAPIView, ProfileAPIView, FileUploadView, \
    ListApiView

app_name='posts'

urlpatterns = [
    path('', views.post_list, name="new-post"),
    path('new-post/', views.post_new, name="new-post"),
    # path('question', views.get_question),
    path('question', GetQuestionAPIView.as_view()),
    path('registration', RegistrationAPIView.as_view()),
    path('login', LoginAPIView.as_view()),
    path('logout', LogoutAPIView.as_view()),
    path('profile', ProfileAPIView.as_view()),
    path('list', ListApiView.as_view()),
    path('upload/<filename>', FileUploadView.as_view(), name='file_upload'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
