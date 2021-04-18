from django.forms import ModelForm, fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django import forms
from django import forms
from .models import *
from django.contrib.admin.widgets import AdminDateWidget
from django.core.exceptions import NON_FIELD_ERRORS





class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

 
 
class catname(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2', 'last_name'  ]

class NameForm (forms.ModelForm):
	class Meta:
         model = Name
         fields = [ 'first_name', 'lastname',  'email']

class studentForm (forms.ModelForm):
	class Meta:
         model = student
         fields = [ 'first_name', 'lastname',  'email']

	 
 

class HotelForm(forms.ModelForm):

	class Meta:
		model = Hotel
		fields = ['name', 'hotel_Main_Img']


class AuthorForm(forms.ModelForm):
	# date = forms.DateField(initial=datetime.date.today, widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Author
        fields = [ 'title',    'name',  'city' , 'address'   , 'description' ]
	
	
     
 

class AmiForm(forms.ModelForm):

	 class Meta:
		 model = Ami
		 fields=['name', 'email', 'first_name' , 'last_name' , 'date_joined' ,'is_active']
		 error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            }
        }



























































# class SignUpForm(UserCreationForm):
#     first_name = forms.CharField(max_length=32, help_text='First name')
#     last_name = forms.CharField(max_length=32, help_text='Last name')
#     email = forms.EmailField(max_length=64, help_text='Enter a valid email address')

#     class Meta(UserCreationForm.Meta):
#         model = User
#         # I've tried both of these 'fields' declaration, result is the same
#         # fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
#         fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email',)

#         widgets = {
#             'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
#             'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
#             'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
#             'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
#             'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
#             'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'}),
#         }
# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('/')
#     else:
#         form = SignUpForm()
#     return render

# class SignUpForm(UserCreationForm):
#     username = forms.CharField(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
#     first_name = forms.CharField(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}), max_length=32, help_text='First name')
#     last_name=forms.CharField(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}), max_length=32, help_text='Last name')
#     email=forms.EmailField(forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}), max_length=64, help_text='Enter a valid email address')
#     password1=forms.CharField(forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
#     password2=forms.CharField(forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'}))

#     class Meta(UserCreationForm.Meta):
#         model = User
#         # I've tried both of these 'fields' declaration, result is the same
#         # fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
#         fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email',)