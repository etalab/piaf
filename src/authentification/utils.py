from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from .tokens import account_activation_token
from django.contrib.auth import get_user_model
from django.urls import reverse
from urllib.parse import urlencode

User = get_user_model()


def activate(request, uidb64, token):
    error = False
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except Exception as e:
        user = None
        error = e
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(request=request, user=user,)
        return redirect('login')
    else:
        if type(error) == TypeError:
            message_num = 1
        elif type(error) == ValueError:
            message_num = 2
        elif type(error) == OverflowError:
            message_num = 3
        elif type(error) == User.DoesNotExist:
            message_num = 4
        else:
            message_num = 5
        print('errormessage is',message_num, 'while error was', error)
        base_url = reverse('login')
        query_string =  urlencode({'messageid': message_num})
        url = '{}?{}'.format(base_url, query_string)
        return redirect(url)
        # return render(request, 'validate_mail_address_invalid.html')
