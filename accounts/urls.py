from django.conf.urls import patterns, url


# Settings routes
urlpatterns = patterns(
    'accounts.views',
    url(
        r'^settings/',
        'account_settings',
        name='account-settings'
    ),
)
