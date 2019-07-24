from django.db import models
from django.db.models import signals
from django.utils import timezone

from bio.signals import count_changes


class EquipmentCategory(models.Model):
    name = models.CharField(max_length=50)
    equipment_count = models.IntegerField(default=0, editable=False)

    def count_changes(self):
        count = self.equipment_set.count()
        self.equipment_count = count
        self.save()

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return '{}'.format(self.name)


class EquipmentInfo(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    Equipments_items = models.ManyToManyField('EquipmentInfoItems', blank=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return '{}'.format(self.name)


class EquipmentInfoItems(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return '{}'.format(self.title)


class Equipment(models.Model):
    image          = models.TextField(null=True, blank=True)
    name           = models.CharField(max_length=100)
    slug           = models.CharField(max_length=200, default='')
    description    = models.TextField()
    link           = models.TextField()
    category       = models.ForeignKey(EquipmentCategory, on_delete=models.SET_NULL, null=True)
    equipments_info = models.ManyToManyField('EquipmentInfo', blank=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return '{}'.format(self.name)


signals.post_save.connect(count_changes, sender=Equipment)

class FavoriteEquipment(models.Model):
    image       = models.TextField(null=True, blank=True)
    title       = models.CharField(max_length=200)
    description = models.TextField()
    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)
    publish     = models.DateTimeField(default=timezone.now)
    link        = models.URLField()

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return '{}'.format(self.title)


class EquipmentUseful(models.Model):
    image          = models.TextField(null=True, blank=True)
    name           = models.CharField(max_length=100)
    description    = models.TextField()
    link           = models.TextField()
    equipments_info = models.ManyToManyField('EquipmentInfo')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return '{}'.format(self.name)



class Magazine(models.Model):
    image       = models.TextField(null=True, blank=True)
    title       = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return '{}, ({})'.format(self.title, self.description)


class MagazineInfo(models.Model):
    image  = models.TextField(null=True, blank=True)
    number = models.IntegerField(default=1)
    title  = models.CharField(max_length=200)
    body   = models.CharField(max_length=200)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return '{}, ({})'.format(self.title, self.body)
