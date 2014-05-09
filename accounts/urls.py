from django.conf.urls import patterns, url
from django.contrib.auth import views as auth_views

from .forms import CustomAuthenticationForm
from .views import CustomUserUpdateView

# Settings routes
urlpatterns = patterns(
    'accounts.views',
    url(
        r'^settings/',
        'account_settings',
    url(
        r'^settings/(?P<pk>\d+)$',
        CustomUserUpdateView.as_view(),
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
