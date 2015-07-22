from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from timezone_field import TimeZoneField

from constants import COLORS


class Project(models.Model):
    # from http://ios7colors.com
    COLOR_CHOICES = map(lambda x: (x, x), COLORS.keys())
    DEFAULT_COLOR = COLOR_CHOICES[0][0]
    user = models.ForeignKey(User, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    color = models.CharField(null=True, choices=COLOR_CHOICES, max_length=18)

    def __unicode__(self):
        return self.name


class TrackedTime(models.Model):
    user = models.ForeignKey(User)
    project = models.ForeignKey(Project, null=True)
    track_date = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    hours = models.FloatField(validators=[MinValueValidator(0)])
    satisfaction = models.IntegerField(default=0)
    # tags = models.CharField(max_length=255,default='')
    description = models.CharField(max_length=255, default='')
    manual_date = models.BooleanField(default=False)
    deleted_project_id = models.IntegerField(null=True)
    indicators = models.ManyToManyField('Indicator', through='IndicatorToTrackedtime')


class Timezone(models.Model):
    user = models.ForeignKey(User)
    timezone = TimeZoneField(default='Europe/London')


class Tag(models.Model):
    name = models.CharField(max_length=255)
    times = models.ManyToManyField(TrackedTime)

class Domain(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['pk']

    def __unicode__(self):
        return self.name

class Indicator(models.Model):
    domain = models.ForeignKey(Domain)
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=6, default="95CEFF")

    class Meta:
        ordering = ['pk']

    def __unicode__(self):
        return self.name

class IndicatorToTrackedtime(models.Model):
    tracked_time = models.ForeignKey(TrackedTime)
    indicator = models.ForeignKey(Indicator)
    value = models.PositiveSmallIntegerField(default=50)
