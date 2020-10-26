from django.db import models
from django.conf import settings

from users.models import UserProfile


class Poll(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    desc = models.TextField(null=True, blank=True)

    NON_EDITABLE_FIELDS = ('start_date', )

    # Validate NON_EDITABLE_FIELDS are not modified
    def update(self, **kwargs):
        for key, value in kwargs.items():
            if key in self.NON_EDITABLE_FIELDS:
                continue
            setattr(self, key, value)
        self.save(update_fields=kwargs.keys())

    def __str__(self):
        desc = f'{self.desc}'
        if len(self.desc) > 10:
            return f'{desc}...'
        return desc

    class Meta:
        verbose_name = 'Poll'


class Question(models.Model):
    poll = models.ForeignKey(
        Poll,
        on_delete=models.CASCADE,
        related_name='polls'
    )
    text = models.TextField()
    kind = models.PositiveIntegerField(
        choices=settings.QUESTION_KIND,
        default=settings.TEXT,
    )

    def __str__(self):
        return f'{self.text}'

    class Meta:
        verbose_name = 'Question'


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    value = models.TextField()
    user_identifier = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = 'Answer'
