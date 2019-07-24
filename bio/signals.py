from django.db.models import signals
from django.dispatch import dispatcher

def count_changes(sender, instance, signal, *args, **kwargs):
  """
  Runs through all the change types and adds up their current numbers
  """
  from bio.models import EquipmentCategory
  for change_type in EquipmentCategory.objects.all():
    change_type.count_changes()
