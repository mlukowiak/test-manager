from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from users import views as user_views
from api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('scenarios', views.ScenarioView)
router.register('testcases', views.TestCaseView)
router.register('users', views.UserView)
router.register('s_type', views.ScenarioTypeView)
router.register('s_area', views.ScenarioAreaView)

urlpatterns = [
    path('', include('testmanager.urls')),
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    #path('scenarios/api/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)