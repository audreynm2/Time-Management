from django.db import models

from django.db import models

class MissionObjective(models.Model):
    # Astronaut/Space theme names!
    title = models.CharField(max_length=200) 
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
