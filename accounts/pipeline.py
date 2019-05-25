from django.contrib import messages


def social_user_save(backend, user, response, *args, **kwargs):
    """save user from social apps"""
    user_data = f"{response['first_name']} {response['last_name']}"
    if kwargs['is_new']:
        messages.success(kwargs['request'], f'You are registered as <strong>{user_data}</strong>')
    else:
        messages.success(kwargs['request'], f'You are logged in as <strong>{user_data}</strong>')

    if backend.name == 'vk-oauth2':
        user.social_pict = response['photo_200']
        user.social_id = response['user_id']
    user.is_active = True
    user.is_verified = True
    user.save()
