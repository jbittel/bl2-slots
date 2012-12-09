from django.db import models


SLOTS_TYPE = (('T', 'Torgue'),
              ('M', 'Moxxi'))

SLOTS = ((0, 'Cherries'),
         (1, 'Marcus'),
         (2, 'Bell'),
         (3, 'Vault'),
         (4, 'Psycho'),
         (5, 'Leg'),
         (6, 'Seven'),
         (7, 'Eridium x3'),
         (8, 'Eridium x2'),
         (9, 'Eridium x1'))


class RecordSlotsModel(models.Model):
    sa = models.IntegerField('1st', choices=SLOTS, default=None)
    sb = models.IntegerField('2nd', choices=SLOTS, default=None)
    sc = models.IntegerField('3rd', choices=SLOTS, default=None)
    slots_type = models.CharField(max_length=1, choices=SLOTS_TYPE)
    client_ip = models.IPAddressField()
