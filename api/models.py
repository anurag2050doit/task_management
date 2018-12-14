from django.db import models
from django.db.models import Sum


# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=50, unique=True)
    is_deleted = models.BooleanField(default=False)

    def delete(self, *args, **kwargs):
        """ Soft delete """
        self.is_deleted = True
        self.save()

    def __str__(self):
        return '%s' % self.category

    def __unicode__(self):
        return '%s' % self.category


class Tag(models.Model):
    tag = models.CharField(max_length=50, unique=True)
    is_deleted = models.BooleanField(default=False)

    def delete(self, *args, **kwargs):
        """ Soft delete """
        self.is_deleted = True
        self.save()

    def __str__(self):
        return '%s' % self.tag

    def __unicode__(self):
        return '%s' % self.tag


class Task(models.Model):
    PRIORITY_CHOICES = (
        (1, 'Blocker'),
        (2, 'Critical'),
        (3, 'Major'),
        (4, 'Minor')
    )
    TASK_STATUS_CHOICES = (
        ('BL', 'Blocked'),
        ('OP', 'Open'),
        ('IP', 'In Progress'),
        ('IR', 'In Review'),
        ('CL', 'Closed')
    )

    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=254)
    description = models.TextField(blank=True)
    priority = models.PositiveIntegerField(choices=PRIORITY_CHOICES, default=4)
    task_status = models.CharField(max_length=2, choices=TASK_STATUS_CHOICES, default='OP')
    category = models.ManyToManyField('Category', blank=True, related_name='categories')
    tag = models.ManyToManyField('Tag', blank=True, related_name='tags')
    created_by = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='creator')
    assigned_to = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='assignee')

    class Meta:
        ordering = ['priority', '-modified_at']

    def delete(self, *args, **kwargs):
        """ Soft delete """
        self.is_deleted = True
        self.save()

    def __str__(self):
        return '%d. %s' % (self.pk, self.title)
