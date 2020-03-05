from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile
from django.core.mail import send_mail
import random
# from myapp.models import Restaurant_review
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        otp = random.randint(100000, 999999)
        p = Profile.objects.create(user=instance, otp=otp)
        instance.set_password(instance.password)
        instance.save()
        p.save()
        send_mail(
            'OTP',
            'OTP foy you is:'+str(otp),
            'pooja.rana@ia.ooo',
            ['to@example.com'],
            fail_silently=False,
        )
 
