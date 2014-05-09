from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.views.generic import UpdateView

from .forms import CustomUserUpdateForm
from .models import CustomUser


@login_required
def user_settings(request):
    return HttpResponseRedirect(
        '%s%s' % ('settings/', request.user.pk)
    )


class CustomUserUpdateView(UpdateView):
    model = CustomUser
    form_class = CustomUserUpdateForm
    template_name = 'accounts/settings.html'

    def get_success_url(self):
        return reverse('account-settings', args=[self.object.id, ])
