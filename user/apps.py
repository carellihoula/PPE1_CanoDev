from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user'

    def ready(self):
        import user.signals


"""@receiver(post_save, sender = Profile)
def createProfile(sender, instance, created, **kwargs):
    if created:
        #user = instance
        Profile.objects.create(user = instance)"""
        