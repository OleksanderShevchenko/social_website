from django import forms
from django.contrib.auth import get_user_model


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):  # create new form for new user registration basing on UserModel
    # two new fields to user model to get password for new user and validate them to be the same
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()  # get UserModel dynamically and include mentioned fields of the model to the form
        fields = ['username', 'first_name', 'email']

    def clean_password2(self):
        """
        Password validation method for field 'pasword2'.
         The method calls automatically on form validation
        :return: second password cleaned
        :raise forms.ValidationError: if password is not correct
        """
        cd = self.cleaned_data

        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Passwords don't match.")
        return cd['password2']
