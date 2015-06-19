from django.db import models


class ChairState(models.Model):
    in_use = models.BooleanField(default=True)
    acc = models.IntegerField(blank=True, null=True, default=0)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        ordering = ['-created']

    def __unicode__(self):
        return u'Used: {} - {} - {}'.format(self.in_use,
                                            self.acc,
                                            self.created)


class Temp(models.Model):
    temp = models.IntegerField(blank=True, null=True, default=0)
    humidity = models.IntegerField(blank=True, null=True, default=0)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        ordering = ['-created']

    def __unicode__(self):
        return u'{}C - {}H'.format(self.temp, self.humidity)
