import attrs
from django.db import transaction

from apps.users import models
from apps.users.domain import value_objects
from domain.base.repository import GenericRepository


class UserRepository(GenericRepository):
    @classmethod
    @transaction.atomic()
    def create(cls, entity: value_objects.CreateUser):
        user = models.User.objects.create(**attrs.asdict(entity))
        return value_objects.User.from_model(user=user)

    @classmethod
    @transaction.atomic()
    def remove(cls, entity):
        pass

    @classmethod
    def get_by_id(cls, id):
        user = models.User.objects.get(id=id)
        return value_objects.User.from_model(user=user)


class TeamRepository(GenericRepository):
    @classmethod
    @transaction.atomic()
    def create(cls, entity: value_objects.CreateTeam):
        team = models.Team.objects.create(team_name=entity.team_name)
        team.members.add(entity.user_id)
        return value_objects.Team.from_model(team=team)

    @classmethod
    @transaction.atomic()
    def remove(cls, entity):
        pass

    @classmethod
    def get_by_id(cls, id):
        team = models.Team.objects.get(id=id)
        return value_objects.Team.from_model(team=team)
