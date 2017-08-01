
**django-esay-account**


![django logo](http://djangostars.com/blog/content/images/2017/03/Screenshot_812123.png)


[see it on pypi  ](https://pypi.python.org/pypi?:action=display&name=django-esay-account&version=0.0.2)


 `django-esay-account is a simple Django app for accounts handle login & SingUp & logout and User Profil tow`

to install the application


`first check the requirements file`

>pip install django-esay-account

![install](https://github.com/mhadiahmed/accounts/blob/master/docs/pip_install.gif)



Quick start
-----------

1. Add "django-esay-account" to your INSTALLED_APPS setting like this::

>    INSTALLED_APPS = [
>        ...


>    'crispy_forms',


>    'account',
>    ]
  
  
  add this line for the crispy_froms



>CRISPY_TEMPLATE_PACK = 'bootstrap3'


![install](https://github.com/mhadiahmed/accounts/blob/master/docs/setting1.gif)


2. Include the accounts URLconf in your project urls.py like this::

>   url(r'^', include('account.urls')),


![install](https://github.com/mhadiahmed/accounts/blob/master/docs/seturls.gif)

3. add this 6 lines at the bottom in the settings files to handel the password reset.


 >EMAIL_BACKEND ='django.core.mail.backends.console.EmailBackend' 
	
 >DEFAULT_FROM_EMAIL = 'example@example.com'
	
 >EMAIL_HOST_USER = ''
	
 >EMAIL_HOST_PASSWORD = ''
	
 >EMAIL_USE_TLS = False 
	
 >EMAIL_PORT = 1025

* and this line for define the media path

>MEDIA_URL = '/media/'



![install](https://github.com/mhadiahmed/accounts/blob/master/docs/settings2.gif)



5. Run `python manage.py migrate` to create the django-esay-account models.



![install](https://github.com/mhadiahmed/accounts/blob/master/docs/migrate.gif)

6. create super user 



![install](https://github.com/mhadiahmed/accounts/blob/master/docs/superuser.gif)

7. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a django-esay-account (you'll need the Admin app enabled).
   
   
![install](https://github.com/mhadiahmed/accounts/blob/master/docs/runserver.gif)


8. Visit http://127.0.0.1:8000/login/ to test the  django-esay-account.



![install](https://github.com/mhadiahmed/accounts/blob/master/docs/login.gif)
