from django.db import models

from web.home import models as home_models

class Submission( models.Model ):
    team = models.ForeignKey( home_models.Team )
    timestamp = models.DateTimeField( auto_now = True )
    sha1sum = models.CharField( max_length=100 )
    data = models.FileField( upload_to='bots' )
    comments = models.TextField()

    def get_score(self):
        # TODO: Query here
        return 0
    score = property(get_score)

    def __unicode__(self):
        return "[Submission %s]"%(self.sha1sum)
    
