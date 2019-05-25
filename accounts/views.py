from django.contrib import messages, auth
from django.http import HttpResponseRedirect
from django.urls import reverse


def logout(request):
    auth.logout(request)
    messages.warning(request, f'You logged out. Bye.')
    return HttpResponseRedirect(reverse('landing:index'))
