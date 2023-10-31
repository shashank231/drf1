from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import LogEntry, Author


@receiver([post_save, post_delete], sender=Author)
def log_changes(sender, instance, created=False, **kwargs):
    print("1111111111111111111111111111111111111111111111111111111111111111111111111")

    signal = kwargs.get('signal')
    if signal == post_delete:
        action = 'deleted'
    else:
        action = 'created' if created else 'updated'
    model = sender.__name__
    instance_id = instance.id
    log_entry = LogEntry(action=action, model=model, instance_id=instance_id)
    log_entry.save()
