from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import permalink
from barnabe.utils import BARNABE_PERMISSION_CHOICES
from churchship.models import Church


class BarnabeUser(models.Model):
    user = models.OneToOneField(User)
    supervisor = models.ForeignKey('self', blank=True, null=True)
    is_supervisor = models.BooleanField(default=True)

    def get_name_display(self):
        name = (self.user.first_name if self.user.first_name is not None else '') + u' ' + (self.user.last_name if self.user.last_name is not None else '')
        if name != ' ':
            return name
        else:
            return self.user.username

    def get_groups_display(self):
        user_groups = self.user.groups.all()
        groups_str = u', '.join([unicode(i.name) for i in user_groups])
        return groups_str

    @permalink
    def get_absolute_url(self):
        return ('barnabeuser_detail', (), {'pk': self.id})

    def __str__(self):
        return self.user.username.encode('utf8')

class BarnabeUserChurch(models.Model):
    barnabe_user = models.ForeignKey(BarnabeUser)
    church = models.ForeignKey(Church)

    def __str__(self):
        return (self.barnabe_user.user.username + u" em " + self.church.name).encode('utf8')