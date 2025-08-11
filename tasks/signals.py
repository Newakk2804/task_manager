from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from tasks.models import Task


@receiver(post_save, sender=Task)
def task_post_save(sender, instance, created, **kwargs):
    if created:
        subject = f"Создана новая задача: {instance.title}"
        message = (
            f"Пользователь {instance.owner.username} создал задачу:\n\n"
            f"Заголовок: {instance.title}\n"
            f"Описание: {instance.description or '-'}\n"
            f"Срок: {instance.due_date or 'or'}\n"
        )
        recipient = None
        if getattr(instance.owner, "email", None):
            recipient = [instance.owner.email]
        if recipient:
            from_email = getattr(settings, "DEFAULT_FROM_EMAIL", "noreply@localhost")
            send_mail(subject, message, from_email, recipient, fail_silently=True)
        else:
            print(
                f"[signals] Задача '{instance.title}' создана пользователем {instance.owner.username} (email не указан)"
            )
