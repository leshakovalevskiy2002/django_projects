from django.urls import reverse
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django_celery.celery import app


@app.task
def send_verification_email(user_id):
    User = get_user_model()
    try:
        user = User.objects.get(pk=user_id)
        send_mail(
            'Verify your account',
            'Follow this link to verify your account: '
            'http://localhost:8000%s' % reverse('verify', kwargs={'uuid': str(user.verification_uuid)}),
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently=False,
        )
    except User.DoesNotExist:
        print("Tried to send verification email to non-existing user '%s'" % user_id)