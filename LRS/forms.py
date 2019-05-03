from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model
)

User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)

            if not user:
                raise forms.ValidationError('User not found')

            if not user.check_password(password):
                raise forms.ValidationError('Password is incorrect')

            if not user.is_active:
                raise forms.ValidationError('User is in active')

            return super(LoginForm, self).clean(*args, **kwargs)


class RegisterForm(forms.ModelForm):
    name = forms.CharField(label="Name")
    email = forms.EmailField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    cpassword = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = [
            'username',
            'name',
            'email',
            'password',
            'cpassword'
        ]

    def clean(self, *args, **kwargs):
        password = self.cleaned_data.get('password')
        cpassword = self.cleaned_data.get('cpassword')
        email = self.cleaned_data.get('email')

        if password != cpassword:
            raise forms.ValidationError("Password do not match")

        email_check = User.objects.filter(email=email)

        if email_check.exists():
            raise forms.ValidationError("email already registered")

        return super(RegisterForm, self).clean(*args, **kwargs)