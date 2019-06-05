from django.db import models
from django.conf import settings


class RPGModule(models.Model):
    """ describe the optional module used for one universe. It can be a ruleset
    or a module for specific periode of time.
    """
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    modules_name = models.TextField(blank=True)
    modules_urls = models.TextField(blank=True)
    is_ruleset = models.BooleanField()

    def __str__(self):
        return self.name


class Universe(models.Model):
    """ describe an universe
    """
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    game_master = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                         related_name='masterised_universes')
    players = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                     related_name='played_universes',
                                     blank=True)
    fork_from = models.ForeignKey("self", related_name='forked',
                                  on_delete=models.CASCADE, blank=True,
                                  null=True)
    modules = models.ManyToManyField(RPGModule, related_name='universes',
                                     blank=True)

    def __str__(self):
        return self.name
