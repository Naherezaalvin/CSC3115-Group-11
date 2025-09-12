from django.db import models

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Program(TimeStampedModel):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    national_alignment = models.CharField(max_length=255, blank=True)
    focus_areas = models.CharField(max_length=255, blank=True)
    phases = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

class Project(TimeStampedModel):
    NATURE_CHOICES = [
        ("research", "Research"),
        ("prototype", "Prototype"),
        ("applied", "Applied Work"),
    ]
    PROTOTYPE_STAGE_CHOICES = [
        ("concept", "Concept"),
        ("prototype", "Prototype"),
        ("mvp", "MVP"),
        ("launch", "Market Launch"),
    ]

    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name="projects")
    title = models.CharField(max_length=200)
    nature_of_project = models.CharField(max_length=20, choices=NATURE_CHOICES, default="prototype")
    description = models.TextField(blank=True)
    innovation_focus = models.CharField(max_length=255, blank=True)
    prototype_stage = models.CharField(max_length=20, choices=PROTOTYPE_STAGE_CHOICES, default="concept")
    testing_requirements = models.TextField(blank=True)
    commercialization_plan = models.TextField(blank=True)

    def __str__(self):
        return self.title


def outcome_artifact_upload_to(instance, filename):
    return f"outcomes/{instance.project_id}/{filename}"


class Outcome(TimeStampedModel):
    OUTCOME_TYPE_CHOICES = [
        ("cad", "CAD"),
        ("pcb", "PCB"),
        ("prototype", "Prototype"),
        ("report", "Report"),
        ("business_plan", "Business Plan"),
    ]
    COMMERCIALIZATION_STATUS_CHOICES = [
        ("demoed", "Demoed"),
        ("market_linked", "Market Linked"),
        ("launched", "Launched"),
        ("na", "Not Applicable"),
    ]

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="outcomes")
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    artifact_file = models.FileField(upload_to=outcome_artifact_upload_to, blank=True, null=True)
    artifact_link = models.URLField(blank=True)
    outcome_type = models.CharField(max_length=20, choices=OUTCOME_TYPE_CHOICES)
    quality_certification = models.CharField(max_length=255, blank=True)
    commercialization_status = models.CharField(
        max_length=20, choices=COMMERCIALIZATION_STATUS_CHOICES, default="na"
    )

    def __str__(self):
        return f"{self.title} (Project #{self.project_id})"

