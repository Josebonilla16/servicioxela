from django.conf.urls import include ,url
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView
from django.contrib.auth import views

urlpatterns = [
    url(r'^admin/',admin.site.urls),
    url(r'^accounts/login/$', views.LoginView.as_view(), name='login'),
    url(r'^accounts/logout/$', views.LogoutView.as_view(), name='logout', kwargs={'next_page': 'http://localhost:8000/accounts/login/'}),
    url(r'', include('servicios.urls')),
]

#from django.contrib import admin

#from django.conf.urls import include ,url

#urlpatterns = [
    # Examples:
    # url(r'^$', 'misitio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^accounts/login/$', views.login, name='login'),
    #url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': 'http://localhost:8000/accounts/login/'}),
    #url(r'',include('servicios.urls')),
#]
