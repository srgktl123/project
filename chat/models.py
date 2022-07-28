from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class Chat(models.Model):
    DIALOG = 'D'
    CHAT = 'C'
    CHAT_TYPE_CHOICES = (
        (DIALOG, _('Dialog')),
        (CHAT, _('Chat'))
    )

    type = models.CharField(
        _('type'),
        max_length=1,
        choices=CHAT_TYPE_CHOICES,
        default=DIALOG
    )
    members = models.ManyToManyField(User, verbose_name=_("Participant"))

    def __str__(self):
        return 'members:[{}] - {}'.format(', '.join(self.members.all().values_list('username', flat=True)),self.type)
    class Meta:
        ordering = ['???? by pub_date of message ????']




class Message(models.Model):
    chat = models.ForeignKey(Chat, verbose_name=_("chat de discussion"),on_delete=models.CASCADE)
    author = models.ForeignKey(User, verbose_name=_("utilisateur"),on_delete=models.CASCADE)
    message = models.TextField(_("Message"))
    pub_date = models.DateTimeField(_('date de creation'), default=timezone.now)
    is_readed = models.BooleanField(_('Lu'), default=False)

    class Meta:
        ordering=['pub_date']

    def __str__(self):
        return self.message