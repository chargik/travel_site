from django.db import models
# Create your models here.
MANAGER_CHOICE = (
    ("Майя", "Майя"),
    ("Вероника", "Вероника"),
    ("Ирина", "Ирина"),
    ("-", "-")
    )


class Join(models.Model):
    lead_name = models.CharField(max_length=50, blank=True)
    telephone = models.CharField(max_length=17, blank=True)
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)
    manager = models.CharField(max_length=20, choices=MANAGER_CHOICE, default='-')
    tour_direction = models.CharField(max_length=20, blank=True)
    updated = models.DateTimeField(auto_now=True)

    # python manage.py makemigrations

    def __str__(self):
        return self.lead_name


    class Meta:
        verbose_name_plural = 'leads'
        ordering = ["-timestamp"]
