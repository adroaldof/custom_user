from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.views.generic import UpdateView

from .forms import CustomUserUpdateForm, CustomUserCreationForm
from .models import CustomUser


@login_required
def user_settings(request):
    return HttpResponseRedirect('settings/%s' % request.user.pk)


class CustomUserUpdateView(UpdateView):
    model = CustomUser
    form_class = CustomUserUpdateForm
    template_name = 'accounts/settings.html'

    def get_success_url(self):
        return reverse('account-settings', args=[self.object.id, ])


def registrate(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = auth.authenticate(
                username=form.cleaned_data['email'],
                password=form.cleaned_data['password1']
            )
            auth.login(request, user)
            return HttpResponseRedirect('settings/%s' % request.user.pk)

    args = {}
    args.update(csrf(request))
    args['form'] = CustomUserCreationForm(request.POST)

    return TemplateResponse(request, 'registration/registrate.html', args)
