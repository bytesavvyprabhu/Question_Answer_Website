from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, UserModel

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
       created = UserModel.objects.get_or_create(user=instance)