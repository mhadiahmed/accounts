from django.conf.urls import url,include
from django.contrib.auth.views import (
	password_reset,password_reset_done,
	password_reset_confirm,password_reset_complete)
from account import views
from django.conf.urls.static import static 
from django.conf import settings


urlpatterns = [
    url(r'^login/$',views.login_view,name='login'),
    url(r'^accounts/login/$',views.login_view,name='login'),
    url(r'^logout/$',views.logout_view,name='logout'),
    url(r'^custmize/$',views.edit_all,name='custmize'),
    url(r'^profile/$',views.profile , name='profile'),
	url(r'^profile/(?P<pk>\d+)/$',views.profile , name='profile_pk'),
	url(r'^edit/profile/$',views.editProfile , name='edit_profile'),
	url(r'^edit/password/$',views.ChangePassword , name='change_password'),
    url(r'^password-reset/done/$',password_reset_done ,{'template_name':'password/password_sent.html'}, name='password_reset_done'),
	url(r'^password-reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',password_reset_confirm ,{'template_name':'password/password_confirm.html'}, name='password_reset_confirm'),
	url(r'^password-reset/$',password_reset,{'template_name':'password/password_reset.html'} , name='password-reset'),
	url(r'^password_reset/complete/$',password_reset_complete,{'template_name':'password/password_complete.html'} , name='password_reset_complete'),
    ]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)