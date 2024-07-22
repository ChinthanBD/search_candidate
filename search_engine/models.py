from django.db import models


# Create your models here.
class Candidate(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.name

# ["Ajay Kumar Yadav", "Ajay Kumar Sharma", "Kumar Sharma Yadav", "Ajay Singh", "Rajesh Yadav"]
# Candidate.objects.create(name = "Ajay Kumar Yadav")
# Candidate.objects.create(name = "Ajay Kumar Sharma")
# Candidate.objects.create(name = "Kumar Sharma Yadav")
# Candidate.objects.create(name = "Ajay Singh")
# Candidate.objects.create(name = "Rajesh Yadav")

    
