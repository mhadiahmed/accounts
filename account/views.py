from django.contrib.auth import(
	authenticate,
	get_user_model,
	login,
	logout,
	)
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from .forms import UserLoginForm,UserRigester,UserProfile,EditProfileForm
from django.shortcuts import render,redirect
from django.db.models import Q
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from django.contrib.auth.decorators import login_required
User = get_user_model()
def login_view(request):
	next = request.GET.get('next')
	title = "Login"
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get('password')
		user = authenticate(username=username,password=password)
		login(request,user)
		if next:
			redirect(next)
		return redirect("profile")
	return render(request,"login.html",{"form":form,"title":title})

def register_view(request):
	next = request.GET.get("next")
	title = "SingUp"
	form = UserRigester(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user.set_password(password)
		user.is_staff=True
		user.save()
		new_user = authenticate(username=user.username,password=password)
		login(request,new_user)
		if next:
			redirect(next)
		return redirect("profile")
	return render(request,"singup.html",{"title":title,"form":form})


def logout_view(request):
	logout(request)
	return redirect("login")
	
@login_required
def profile(request,pk=None):
	if pk:
		user = User.objects.get(pk=pk)
	else:
	  	user = request.user
	if not user.is_authenticated():
		respons = render_to_response("noprofile.html",{"title":"Not Fonde 404"})
		respons.status_code = 403
		return respons
	
	
	context = {
		"title":"profile",
		"user":user,
	}
	return render(request,"profile.html",context)
@login_required
def editProfile(request):

	if request.method == 'POST':
		form = EditProfileForm(request.POST, instance=request.user)

		if form.is_valid():
			form.save()
			messages.success(request,"Successfully Updated")
			return redirect('profile')
	else:
		form = EditProfileForm(instance=request.user)
	context = {
	"forms":form,
	"title":"Edit Profile"
	}
	return render(request,"edit_profile.html",context)


#ChangePassword

def ChangePassword(request):
	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)

		if form.is_valid():
			form.save()
			update_session_auth_hash(request,form.user)
			return redirect('profile')
		else:
			return redirect('change_password')
	else:
		form = PasswordChangeForm(user=request.user)
		context = {
		"forms":form,
		"title":"Change Password"
		}
		return render(request,"Change_pass.html",context)

@login_required
def edit_all(request):
	title = "custmize Profile"
	try:
		profile = request.user.userprofile
	except UserProfile.DoesNotExist:
		profile = UserProfile(user=request.user)

	if request.method == 'POST':
	    form = UserProfile(request.POST or None, request.FILES or None,instance=profile)
	    if form.is_valid():
	        form.save()
	        return redirect("profile")
	else:
	    form = UserProfile(instance=profile)
	return render(request,'editall.html',{'title':title,"form":form})



