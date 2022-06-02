from email.policy import default
from random import choices
from django.db import models
import uuid
from user.models import Profile
from django.contrib.auth.models import User


""" Les models nous permet de créer les entrées dans notre base de données : 
 ils permettent la creations de nos tables de base de données."""

#Notre class (tableau) qui contient tout les éléments d'un Projet (Project)

class Project(models.Model):
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=300)
    description = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(null=True, blank=True, default="default.jpg")
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    vote_total = models.IntegerField(default=0, null = True, blank=True)
    vote_ratio = models.IntegerField(default=0, null = True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    

    def __str__(self) :
        return (f"{self.title} : {self.owner}")

    

    #pour classer nos projets par ordre d'ancienneté : 
    # ['-created'] 

    class Meta : 
        ordering = ['-vote_ratio', '-vote_total', 'title'] # ['-created'] pour faire l'inverse

    def reviewers(self):
        queryset = self.review_set.all().values_list('owner__id', flat=True)


    @property
    def getVoteCount(self):
        reviews = self.review_set.all()
        upVotes = reviews.filter(value='up').count()
        totalVotes = reviews.count()

        ratio = (upVotes / totalVotes) * 100
        self.vote_total = totalVotes
        self.vote_ratio = ratio

        self.save()


class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote')
    )
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    project= models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=300, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='like')
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    """Pour un seul commentaire pour un seul utilisateur : 
    class Meta:
        unique_together = [['owner', 'project']]"""


    def __str__(self):
        return f" {self.project} : {self.value}"
    
    def total_likes(self):
        return self.likes.count()

#tableau outils utilisés pour réaliser le projet

class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name
