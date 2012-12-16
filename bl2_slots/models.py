import decimal
import json

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


class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        """
        Convert Decimal instances to floats, formatting them
        to two decimal places.
        """
        if isinstance(obj, decimal.Decimal):
            return round(float(obj), 2)
        return super(DecimalEncoder, self).default(obj)

class OutcomesManager(models.Manager):
    def as_json(self):
        """
        Output table data as a JSON array of objects.
        """
        outcomes = []
        for obj in self.all():
            outcome = dict([(field, val) for field, val in obj])
            outcomes.append(outcome)
        return json.dumps(outcomes, cls=DecimalEncoder)

class AbstractOutcomes(models.Model):
    symbols = models.CharField(max_length=3, choices=SYMBOLS)
    chance = models.DecimalField(max_digits=4, decimal_places=2)
    reward = models.CharField(max_length=30)

    objects = OutcomesManager()

    class Meta:
        abstract = True

    def __iter__(self):
        for i in self._meta.get_all_field_names():
            if i == 'id': # Ignore the id field
                continue
            yield (i, getattr(self, i))

class MoxxiOutcomes(AbstractOutcomes):
    pass

class TorgueOutcomes(AbstractOutcomes):
    pass

class RecordSlotsModel(models.Model):
    sa = models.IntegerField('1st', choices=SLOTS, default=None)
    sb = models.IntegerField('2nd', choices=SLOTS, default=None)
    sc = models.IntegerField('3rd', choices=SLOTS, default=None)
    slots_type = models.CharField(max_length=1, choices=SLOTS_TYPE)
    client_ip = models.IPAddressField()
