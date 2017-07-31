Quick start
-----------

1. Add "django-esay-accounts" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
    'crispy_forms',
    'account',
    ]
  add this line for the crispy_froms

	CRISPY_TEMPLATE_PACK = 'bootstrap3'

2. Include the accounts URLconf in your project urls.py like this::

    url(r'^', include('account.urls')),
   add this line to the main urls conf tow
   from django.conf.urls.static import static 
   from django.conf import settings

   if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)