# Generated by Django 4.2.4 on 2023-08-06 21:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ('djstripe', '0012_2_8'),
        ('users', '0002_user_company_user_created_at_user_phone_number_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                (
                    'customer',
                    models.ForeignKey(
                        blank=True,
                        help_text="The member's Stripe Customer object for this team, if it exists",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to='djstripe.customer',
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=100)),
                (
                    'members',
                    models.ManyToManyField(
                        related_name='teams', through='users.Membership', to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    'subscription',
                    models.ForeignKey(
                        blank=True,
                        help_text="The team's Stripe Subscription object, if it exists",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to='djstripe.subscription',
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name='membership',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.team'),
        ),
        migrations.AddField(
            model_name='membership',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]