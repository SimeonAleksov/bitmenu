from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_tenants.models import DomainMixin
from django_tenants.models import TenantMixin


class User(AbstractUser):
    name = models.CharField(_('Name of User'), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    company = models.CharField(_('Company of User'), blank=True, max_length=255)
    phone_number = models.CharField(_('Phone number'), blank=True, max_length=255)


class Team(models.Model):
    team_name = models.CharField(max_length=100)
    members = models.ManyToManyField(
        'User',
        related_name='teams',
        through='Membership',
    )
    subscription = models.ForeignKey(
        'djstripe.Subscription',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text="The team's Stripe Subscription object, if it exists",
    )


class Membership(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    customer = models.ForeignKey(
        'djstripe.Customer',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text="The member's Stripe Customer object for this team, if it exists",
    )


class Client(TenantMixin):
    name = models.CharField(max_length=100)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    paid_until = models.DateField()
    on_trial = models.BooleanField()
    created_on = models.DateField(auto_now_add=True)

    auto_create_schema = True


class Domain(DomainMixin):
    pass
