# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone
import datetime


class Term(models.Model):
    """ Term Class """

    name = models.CharField(max_length=50, verbose_name='名称')
    date_start = models.DateField(verbose_name='开始日期')
    date_end = models.DateField(verbose_name='结束日期')
    type = models.BooleanField(default=False, verbose_name='类型', help_text='是否为假期类型')
    date_added = models.DateTimeField(default=datetime.date.today(), verbose_name='注册日期')

    class Meta:
        verbose_name = '学期'
        verbose_name_plural = '学期'
        ordering = ('date_added', 'type',)

    def __unicode__(self):
        return "%s" % self.name

    def __str__(self):
        return "%s" % self.name

    def exact_type(self):
        """ Return the name of a team type """
        if self.type:
            return '假期'
        else:
            return '学期'

    exact_type.admin_order_field = 'type'
    exact_type.short_description = '类型'

    def was_added_recently(self):
        """ Determine whether a team was added recently """
        return self.date_added >= timezone.now() - datetime.timedelta(days=1)

    was_added_recently.admin_order_field = 'date_added'
    was_added_recently.boolean = True
    was_added_recently.short_description = '最近注册？'

    def current_week(self):
        """ A function to calculate the current week and return it """
        today = datetime.date.today()
        delta = today - self.date_start
        if delta.days % 7:
            return delta.days / 7 + 1
        else:
            return delta.days / 7



class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name='名称')
    user = models.ForeignKey(User, verbose_name='用户')
    location = models.CharField(max_length=50, verbose_name='教室')
    weeks = models.CharField(max_length=100, verbose_name='周次')
    weekday = models.CharField(max_length=10, verbose_name='星期')
    grid = models.CharField(max_length=30, verbose_name='节次')
    time_start = models.TimeField(verbose_name='开始时间')
    time_end = models.TimeField(verbose_name='结束时间')
    term = models.ForeignKey(Term, verbose_name='学期')

    def __unicode__(self):
        return self.name