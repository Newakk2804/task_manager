from django.db import models
from django.conf import settings
from django.urls import reverse


class Task(models.Model):
    PRIORITY_LOW = "low"
    PRIORITY_MED = "med"
    PRIORITY_HIGH = "high"

    PRIORITY_CHOISE = [
        (PRIORITY_LOW, "Низкий"),
        (PRIORITY_MED, "Средний"),
        (PRIORITY_HIGH, "Высокий"),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    priority = models.CharField(
        max_length=4, choices=PRIORITY_CHOISE, default=PRIORITY_MED
    )
    due_date = models.DateField(null=True, blank=True)
    owner = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="tasks"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("task_detail", args=[str(self.pk)])
