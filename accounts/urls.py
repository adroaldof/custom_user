from django.conf.urls import patterns, url
from django.contrib.auth import views as auth_views

from .forms import CustomAuthenticationForm
from .views import CustomUserUpdateView

# Settings routes
urlpatterns = patterns(
    'accounts.views',
    url(
        r'^user$',
        'user_settings'
    ),
    url(
        r'^settings/(?P<pk>\d+)$',
        CustomUserUpdateView.as_view(),
        name='account-settings'
    ),
)

# Login/Logout routes
urlpatterns += patterns(
    '',
    url(
        r'^login$',
        auth_views.login,
        {
            'authentication_form': CustomAuthenticationForm,
            'template_name': 'registration/login.html'
        },
        name='login'
    ),
    url(
        r'^logout$',
        auth_views.logout,
        {'template_name': 'registration/logged_out.html'},
        name='logout'
    ),
)

# Deal with accounts
urlpatterns += patterns(
    'accounts.views',
    url(
        r'^registrate$',
        'registrate',
        name="registrate"
    )
)

# Deal with password
urlpatterns += patterns(
    '',
    url(
        r'^password/change$',
        auth_views.password_change,
        {'template_name': 'registration/password_change_form.html'},
        name='password_change'
    ),
    url(
        r'^password/change/done$',
        auth_views.password_change_done,
        {'template_name': 'registration/password_change_done.html'},
        name='password_change_done'
    ),
)
