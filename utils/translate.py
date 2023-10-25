from django.utils.translation import activate


def translate(request):
    try:
        request.LANGUAGE_CODE = request.headers['Accept-Language']
        activate(request.LANGUAGE_CODE)
    except:
        request.LANGUAGE_CODE = 'en-us'
