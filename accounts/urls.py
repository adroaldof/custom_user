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
    url(
        r'^password/reset$',
        auth_views.password_reset,
        {
            'template_name': 'registration/password_reset_form.html',
            'email_template_name': 'registration/password_reset_email.html',
            'subject_template_name': 'registration/password_reset_subject.txt'
        },
        name='password_reset'
    ),
    url(
        r'''^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/
            (?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$''',
        auth_views.password_reset_confirm,
        {'template_name': 'registration/password_reset_confirm.html'},
        name='password_reset_confirm'
    ),
    url(
        r'^password/reset/complete$',
        auth_views.password_reset_complete,
        {'template_name': 'registration/password_reset_complete.html'},
        name='password_reset_complete'
    ),
    url(
        r'^password/reset/done$',
        auth_views.password_reset_done,
        {'template_name': 'registration/password_reset_done.html'},
        name='password_reset_done'
    ),
)
