from django.db.models.signals import post_save
from django.dispath import receiver
from django.core.mail import send_mail
from django.contrib.auth.models import User

from .models import UserResponse



@receiver(pre_save, sender=UserResponse)
def my_handler(sender, instance, created, **kwargs):
    if instance.status is True:
        mail = instance.article.author.email
        send_mail(
            'Subject here',
            'Were is the message.',
            'host@mail.ru',
            [mail],
            fail_silenty=False,
        )

    mail = instance.article.author.email
    send_mail(
        'Subject here',
        'Were is the message.',
        'host@mail.ru',
        [mail],
        fail_silenty=False,
    )