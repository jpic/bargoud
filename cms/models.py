from django.db import models


class Photo(models.Model):
    photo = models.ImageField(upload_to='cms/photo')
    title = models.CharField(max_length=200, null=True, blank=True)
    priority = models.IntegerField(default=0)
    on_home = models.BooleanField(default=False)

    class Meta:
        ordering = ('priority', 'title')

    def __unicode__(self):
        return self.title or "Photo #%s" % self.pk
