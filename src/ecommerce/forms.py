from django import forms

from django.contrib.auth import get_user_model

User = get_user_model()


class ContactForm(forms.Form):
    fullname = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": "Full Name"}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={"class": "form-control", "placeholder": "email"}))
    content = forms.CharField(widget=forms.Textarea(
        attrs={"class": "form-control", "placeholder": "Your content"}))

# custom validation methods

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("Email has to be an gmail account...")
        return email


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password_verify = forms.CharField(
        label="Confirm Password", widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get("username")
        queryset = User.objects.filter(username=username)
        if queryset.exists():
            raise forms.ValidationError(
                "Already exists this username...chose another please")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        queryset = User.objects.filter(email=email)
        if queryset.exists():
            raise forms.ValidationError(
                "Already exists this email...chose another please")

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get("password")
        password_verify = self.cleaned_data.get("password_verify")

        if password_verify != password:
            raise forms.ValidationError("Password must match.")
        return data
