from django.db import models


class SocialNetwork(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class SocialNetworkAccount(models.Model):
    title = models.CharField(max_length=128)
    social_network = models.ForeignKey(
        SocialNetwork,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    link = models.URLField()

    def __str__(self):
        return self.link
