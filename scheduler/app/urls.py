from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.test, name="test"),
    path('task1/', views.scheduleTask, name="test1"),
    path('ping/', views.IP, name="ping"),
    path('register/', views.registerView, name="register"),
    path('login/', views.authlogin, name="login"),
    path('logout/', views.authlogout, name="logout"),
    path('status/', views.viewStatus, name="status"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
