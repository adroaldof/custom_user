from django.conf.urls import patterns, url
from django.contrib.auth import views as auth_views

from .forms import CustomAuthenticationForm

# Settings routes
urlpatterns = patterns(
    'accounts.views',
    url(
        r'^settings/',
        'account_settings',
        name='account-settings'
    ),
)

urlpatterns += patterns(
    '',
    url(
        r'^login/$',
        auth_views.login,
        {
            'authentication_form': CustomAuthenticationForm,
            'template_name': 'registration/login.html'
        },
        name='login'
    ),
    url(
        r'^logout/$',
        auth_views.logout,
        {'template_name': 'registration/loged_out.html'},
        name='logout'
    ),
)
