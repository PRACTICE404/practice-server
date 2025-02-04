from django.db import models

from apps.base.models import Record
from apps.customers.models import Customer


class Marketplace(Record):
    name = models.CharField(max_length=18)
    link = models.URLField()

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name


class MarketplaceAccount(Record):
    name = models.CharField(max_length=64)
    marketplace = models.ForeignKey(Marketplace, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    reviews_count = models.PositiveIntegerField()
    link = models.URLField(blank=True, null=True)

    class Meta:
        ordering = ('is_active', 'reviews_count')

    def __str__(self):
        return f'{self.marketplace} > {self.name}'


class Proposal(Record):
    CHOICES_STATUS = (
        ('1', 'Negotiation'),
        ('2', 'Pending'),
        ('3', 'Succeeded'),
        ('4', 'Expired')
    )

    date_sent = models.DateField()
    customer_title = models.CharField(max_length=128, blank=True, null=True)
    customer_letter = models.TextField()
    customer_feedback = models.BooleanField()
    cover_letter = models.TextField()
    status = models.CharField(max_length=32, choices=CHOICES_STATUS, default='pending')  # NOQA

    marketplace_account = models.ForeignKey(
        MarketplaceAccount,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def __str__(self):
        return f'{self.date_sent} {self.status} {self.marketplace_account or self.customer}'  # NOQA

    class Meta:
        ordering = (
            'status',
            'date_sent',
            'id'
        )
