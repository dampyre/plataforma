from django import forms

#formulario login 

class LoginForm(forms.Form):
		username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nombre Usuario'}))
		password = forms.CharField(widget=forms.PasswordInput(render_value=False, attrs={'placeholder': 'Password'}))