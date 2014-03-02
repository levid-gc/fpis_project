# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


class Record(models.Model):
    user = models.ForeignKey(User)
    date = models.DateField(verbose_name='日期')
    check_in = models.TimeField(verbose_name='签到时间')
    check_out = models.TimeField(verbose_name='签出时间')
