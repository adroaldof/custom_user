from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template.response import TemplateResponse
from django.core.urlresolvers import reverse
from django.views.generic import UpdateView

from .forms import CustomUserUpdateForm
from .models import CustomUser


@login_required
def account_settings(request):
    return TemplateResponse(request, 'accounts/settings.html', {
        'user': request.user,
    })


class CustomUserUpdateView(UpdateView):
    model = CustomUser
    form_class = CustomUserUpdateForm
    template_name = 'accounts/settings.html'

    def get_success_url(self):
        return reverse('account-settings', args=[self.object.id, ])
