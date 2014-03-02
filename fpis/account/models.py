# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone
import datetime


class Team(models.Model):
    """
    Team Class
    """
    id = models.CharField(max_length=10, primary_key=True, verbose_name='编号')
    name = models.CharField(max_length=20, verbose_name='名称')
    type = models.BooleanField(default=False, verbose_name='类型', help_text='是否为导师类型')
    date_added = models.DateTimeField(default=timezone.now, verbose_name='注册日期')

    class Meta:
        verbose_name = '团队'
        verbose_name_plural = '团队'
        ordering = ('id', 'type',)

    def __unicode__(self):
        return "%s" % self.name

    def __str__(self):
        return "%s" % self.name

    def exact_type(self):
        """ Return the name of a team type """
        if self.type:
            return '导师'
        else:
            return '团队'

    exact_type.admin_order_field = 'type'
    exact_type.short_description = '类型'

    def was_added_recently(self):
        """ Determine whether a team was added recently """
        return self.date_added >= timezone.now() - datetime.timedelta(days=1)

    was_added_recently.admin_order_field = 'date_added'
    was_added_recently.boolean = True
    was_added_recently.short_description = '最近注册？'


class UserProfile(models.Model):
    """
    Extend of User Class
    """
    user = models.OneToOneField(User)
    team = models.ForeignKey(Team, verbose_name='团队')

    def __unicode__(self):
        return self.user.username


def create_user_profile(sender, instance, created, **kwargs):
    """Create the UserProfile when a new User is saved"""
    if created:
        profile = UserProfile()
        profile.user = instance
        profile.save()

#post_save.connect(create_user_profile, sender=User)



