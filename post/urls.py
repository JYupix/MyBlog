from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'post'

urlpatterns = [
    path('', views.home_blog, name='home'),
    path('register/', views.register_blog_user, name='register'),
    path('login/', views.login_blog_user, name='login'),
    path('logout/', views.logout_blog_user, name='logout'),
    path('blogs/', views.all_blogs, name='blogs'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
