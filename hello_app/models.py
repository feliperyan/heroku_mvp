from django.db import models

# Create your models here.

class Feedback(models.Model):
    name = models.CharField(max_length=64, blank=False)
    email = models.EmailField(max_length=64, blank=False)
    comments = models.TextField(max_length=140, blank=False)

    wantsServicesXchange = models.BooleanField()
    wantsGoodsXchange = models.BooleanField()
    wantsCharityXchange = models.BooleanField()
    wantsLocationXchange = models.BooleanField()
    wantsBadges = models.BooleanField()
    
    def __unicode__(self):
        return self.name + ' - s:%r g:%r c:%r l:%r b:%r' %(self.wantsServicesXchange,\
            self.wantsGoodsXchange, self.wantsCharityXchange, self.wantsCharityXchange,\
            self.wantsBadges)

