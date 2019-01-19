# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

from django.db import models

from cloud.utils.model_utils import generate_uuid


class Restaurant(models.Model):
    uuid = models.UUIDField(default=generate_uuid)
    store_id = models.CharField(max_length=128, unique=True, blank=False, null=False)
    name = models.CharField(max_length=128, blank=False, null=False)
    is_active = models.BooleanField(default=False)

    class Meta:
        db_table = "restaurant"
