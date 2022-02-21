from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include


#UrlConf

urlpatterns = [
	
	path('', views.profile, name = "profile"),
	path('signup/', views.signup, name = "signup"),
	path('login/', views.login, name = "login"),
	path('logoff/', views.logout_request, name = "logoff"),
	path('profile/<int:uid>', views.profile, name = "profile"),
	path('myprofile/', views.profile_auth, name = "myprofile"),
	path('editprofile/', views.edit_profile_auth, name = "editprofile"),
	path('create/', views.create_auth, name = "create"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)