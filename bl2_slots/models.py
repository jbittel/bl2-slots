from django.db import models


SLOTS_TYPE = (('T', 'Torgue'),
              ('M', 'Moxxi'))

SLOTS = ((0, 'Eridium x3'),
         (1, 'Seven'),
         (2, 'Leg'),
         (3, 'Psycho'),
         (4, 'Vault'),
         (5, 'Bell'),
         (6, 'Marcus'),
         (7, 'Cherries'),
         (8, 'Eridium x1'),
         (9, 'Eridium x2'))

SYMBOLS = (('NNX', '2 same symbols without bell'),
           ('777', '3 cherries'),
           ('222', '3 Moxxi legs'),
           ('666', '3 Marcus'),
           ('444', '3 Vault symbols'),
           ('888', '3 single Eridium'),
           ('999', '3 double Eridium'),
           ('000', '3 triple Eridium'),
           ('NN5', '2 same symbols with bell'),
           ('55X', '2 bells'),
           ('555', '3 bells'),
           ('333', '3 psychos'),
           ('111', '3 sevens'),
           ('XXX', 'No match'))


class MoxxiOutcomes(models.Model):
    symbols = models.CharField(max_length=3, choices=SYMBOLS)
    chance = models.DecimalField(max_digits=4, decimal_places=2)
    reward = models.CharField(max_length=30)

class TorgueOutcomes(models.Model):
    symbols = models.CharField(max_length=3, choices=SYMBOLS)
    chance = models.DecimalField(max_digits=4, decimal_places=2)
    reward = models.CharField(max_length=30)

class RecordSlotsModel(models.Model):
    sa = models.IntegerField('1st', choices=SLOTS, default=None)
    sb = models.IntegerField('2nd', choices=SLOTS, default=None)
    sc = models.IntegerField('3rd', choices=SLOTS, default=None)
    slots_type = models.CharField(max_length=1, choices=SLOTS_TYPE)
    client_ip = models.IPAddressField()
