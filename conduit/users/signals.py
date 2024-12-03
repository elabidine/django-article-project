from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Profile


@receiver(post_save, sender=get_user_model())
def manage_profile_for_user(sender, instance, created, **kwargs):
    """
    Signal to manage user profile creation and saving.
    If a user is created, create a corresponding profile.
    On every save, also save the profile to ensure it's up to date.
    """
    if created:
        # Create a profile for the newly created user
        Profile.objects.create(user=instance)
    else:
        # Save the existing profile to ensure consistency
        instance.profile.save()
