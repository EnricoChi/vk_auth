from django.shortcuts import render, get_object_or_404
from accounts.models import Account


def landing(request):
    if request.user.is_authenticated:
        user = get_object_or_404(Account, social_id=request.user.social_id)
        context = {'object': user}
        return render(request, 'landing/profile.html', {'title': 'Profile', **context})

    return render(request, 'landing/index.html', {'title': 'Sign in please'})
