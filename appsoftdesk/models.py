from django.db import models
from django.conf import settings


class Projects(models.Model):
    """ Project object """

    TYPE_CHOICE = (
        ("Back-end", "Back-end"),
        ("Front-end", "Front-end"),
        ("Mobile", "iOS or Android"),
    )
    title = models.CharField(max_length=250, blank=False, unique=True)
    description = models.CharField(max_length=250, blank=False)
    type = models.CharField(max_length=250, choices=TYPE_CHOICE)
    author_user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title


class Contributors(models.Model):
    """ Contributors linked to a project """

    PERMISSION_CHOICES = (
        ("Creator", "Creator"),
        ("Contributor", "Contributor"),
    )
    author_user = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                             on_delete=models.DO_NOTHING)
    project = models.ForeignKey(to=Projects, on_delete=models.DO_NOTHING,
                                related_name="contributors")
    permission = models.CharField(max_length=15, choices=PERMISSION_CHOICES)
    role = models.CharField(max_length=250)

    def __str__(self):
        return self.project.title

    class Meta:
        unique_together = ('author_user', 'project',)


class Issues(models.Model):
    """ Issues of a project """

    PRIORITY_CHOICES = (
        ("low", "low"),
        ("normal", "normal"),
        ("high", "high"),
    )

    TAG_CHOICES = (
        ("bug", "bug"),
        ("improvement", "improvement"),
        ("task", "task"),
    )

    STATUS_CHOICES = (
        ("to do", "to do"),
        ("in progress", "in progress"),
        ("done", "done"),
    )

    title = models.CharField(max_length=250, unique=True)
    description = models.CharField(max_length=250)
    tag = models.CharField(max_length=250, choices=TAG_CHOICES)
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES)
    project = models.ForeignKey(to=Projects, on_delete=models.CASCADE,
                                related_name="issues")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    author_user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    assignee_user = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                      on_delete=models.DO_NOTHING,
                                         related_name="assignee")
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comments(models.Model):
    """ Comments linked to an issue """

    description = models.CharField(max_length=250)
    author_user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    issue = models.ForeignKey(to=Issues, on_delete=models.CASCADE,
                              related_name="comments")
    created_time = models.DateTimeField(auto_now_add=True)

