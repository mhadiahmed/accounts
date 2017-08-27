from django import forms
from .models import userProfile
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import Permission, User
from django.shortcuts import get_object_or_404
from django.contrib.auth import(
	authenticate,
	get_user_model,
	login,
	logout,
	)

#is_staff()) 

class UserProfile(forms.ModelForm):
	class Meta:
		model = userProfile
		fields = [
			'phone',
			'city',
			'company',
			'image',
		]
		
User = get_user_model()

class UserLoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(
		attrs={'id':'user'}
		))
	password = forms.CharField(widget=forms.PasswordInput(
		attrs={'id':'passlog'}
		))


	def clean(self,*args,**kwargs):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")
		if username and password:
			user = authenticate(username=username,password=password)
			if not user:
				raise forms.ValidationError("this user is not exists")

			if not user.check_password(password):
				raise forms.ValidationError("incorrect password")

			if not user.is_active:
				raise ValidationError("is no longer active")
		return super(UserLoginForm,self).clean(*args, **kwargs)


class UserRigester(forms.ModelForm):
	user = ''
	# permission = Permission.objects.get(name='Can add post')
	# user.user_permissions.add(permission)
	email = forms.EmailField(label="Email Address")
	email2 = forms.EmailField(label="Confirm Email")
	password = forms.CharField(widget=forms.PasswordInput)
	password2 = forms.CharField(widget=forms.PasswordInput,label="Confirm Password")
	class Meta:
		model = User
		fields = [
			'first_name',
			'last_name',
			'username',
			'email',
			'email2',
			'password',
			'password2'
		]



	def clean_password2(self):
		password = self.cleaned_data.get("password")
		
		password2 = self.cleaned_data.get("password2")
		if password != password2:
			raise forms.ValidationError("password must match.")

		return password

	def clean_email2(self):
		email = self.cleaned_data.get("email")
		email2 = self.cleaned_data.get("email2")
		if email != email2:
			raise forms.ValidationError("Emails must match.")

		return email




		def user_gains_perms(request, user_id):
			user = get_object_or_404(User, pk=user_id)
			# any permission check will cache the current set of permissions
			user.has_perm('blog.can_change')

			permission = Permission.objects.get(name='can_change')
			user.user_permissions.add(permission)

class EditProfileForm(UserChangeForm):
	class Meta:
		model = User
		fields=(
			"email",
			"first_name",
			"last_name",
			"password"
			)


