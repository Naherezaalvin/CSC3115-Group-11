from django.db import models

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Program(TimeStampedModel):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    national_alignment = models.CharField(max_length=255, blank=True)
    focus_areas = models.CharField(max_length=255, blank=True)
    phases = models.CharField(max_length=255, blank=True)

    class Meta:
        constraints = [
            # if focus ares is unset, national alignment must be set
            models.CheckConstraint(
                check=(
                    models.Q(focus_areas__isnull=False) | models.Q(national_alignment__isnull=True)
                ),
                name='focus_areas_requires_national_alignment'
            ),
        ]

    def __str__(self):
        return self.name

