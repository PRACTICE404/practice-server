from django.db import models

from apps.base.validators import validate_image_extension


class WorkingExperience(models.Model):
    company_name = models.CharField(max_length=64)
    company_logo = models.ImageField(
        upload_to='website/working-experience/company-logo/',
        validators=[validate_image_extension]
    )
    position_name = models.CharField(max_length=64)
    year_start = models.PositiveIntegerField()
    year_end = models.PositiveIntegerField()
    description = models.TextField()

    class Meta:
        ordering = ('year_start', )

    def __str__(self):
        return self.company_name
