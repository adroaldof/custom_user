from django import forms
from django.contrib.auth.forms import (
    ReadOnlyPasswordHashField, AuthenticationForm
)
from django.forms import TextInput
from django.utils.translation import ugettext_lazy as _

from .models import CustomUser


class CustomUserCreationForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """
    error_messages = {
        'duplicate_useremail': _('A user with that email already exists'),
        'password_mismatch': _("The two password fields didn't match"),
    }
    email = forms.EmailField(
        label=_('Email address'),
        widget=forms.TextInput(
            attrs={'class': 'form-control input-md'}
        ),
        help_text=_('This email will be you username'),
    )
    password1 = forms.CharField(
        label=_('Password'),
        widget=forms.PasswordInput(
            attrs={'class': 'form-control input-md'}
        ),
        help_text=_('Strong password is recommended'),
    )
    password2 = forms.CharField(
        label=_('Password again'),
        widget=forms.PasswordInput(
            attrs={'class': 'form-control input-md'}
        ),
        help_text=_('Enter the same password as above, for verification')
    )

    class Meta:
        # Point to our CustomUser here instead of default `User`
        model = CustomUser
        fields = ('email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')

        try:
            CustomUser._default_manager.get(email=email)
        except CustomUser.DoesNotExist:
            return email
        raise forms.ValidationError(
            self.error_messages['duplicate_useremail'],
            code='duplicate_useremail',
        )

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'])
        return password2

    def save(self, commit=True):
        # Make sure we pass back in our CustomUserCreationForm and not the
        # default `UserCreationForm`
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class CustomUserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        label=_("Password"),
        help_text=_(
            "Raw passwords are not stored, so there is no way to see "
            "this user's password, but you can change the password "
            "using <a href=\"password/\">this form</a>."
        )
    )

    class Meta:
        # Point to our CustomUser here instead of default `User`
        model = CustomUser

    def __init__(self, *args, **kwargs):
        # Make sure we pass back in our CustomUserChangeForm and not the
        # default `UserChangeForm`
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)
        f = self.fields.get('user_permissions', None)
        if f is not None:
            f.queryset = f.queryset.select_related('content_type')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial['password']


class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        # Point to our CustomUser here instead of default `User`
        model = CustomUser
        fields = (
            'full_name', 'short_name', 'email', 'email2', 'phone_cell',
            'phone_home'
        )
        widgets = {
            'full_name': TextInput(attrs={'class': 'form-control input-md'}),
            'short_name': TextInput(attrs={'class': 'form-control input-md'}),
            'email': TextInput(attrs={'class': 'form-control input-md'}),
            'email2': TextInput(attrs={'class': 'form-control input-md'}),
            'phone_cell': TextInput(attrs={'class': 'form-control input-md'}),
            'phone_home': TextInput(attrs={'class': 'form-control input-md'}),
            # 'date_of_birth': TextInput(
            #     attrs={'class': 'form-control input-md'}
            # ),
        }
        exclude = ('password', 'date_joined', 'last_login')


class CustomAuthenticationForm(AuthenticationForm):
    """
    It was extended to show how to do it and to insert class on form fields
    """
    username = forms.CharField(
        label=_('Email address'),
        widget=forms.TextInput(
            attrs={'class': 'form-control input-md'}
        ),
        help_text=_('This email will be you username'),
    )
    password = forms.CharField(
        label=_('Password'),
        widget=forms.PasswordInput(
            attrs={'class': 'form-control input-md'}
        ),
        help_text=_('Strong password is recommended'),
    )
