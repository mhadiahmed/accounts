
**django-esay-accounts**


 > django-esay-accounts is a simple Django app for accounts handle login & SingUp & logout and User Profil tow

to install the application

pip install django-esay-accounts

Quick start
-----------

1. Add "django-esay-accounts" to your INSTALLED_APPS setting like this::

>    INSTALLED_APPS = [
>        ...
>    'crispy_forms',
>    'account',
>    ]
  
  
  add this line for the crispy_froms



>	CRISPY_TEMPLATE_PACK = 'bootstrap3'

2. Include the accounts URLconf in your project urls.py like this::

>   url(r'^', include('account.urls')),
    
   add this line to the main urls conf tow
>   from django.conf.urls.static import static 
>   from django.conf import settings

 

3. Run `python manage.py migrate` to create the django-esay-accounts models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a django-esay-accounts (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/login/ to test the  django-esay-accounts.
