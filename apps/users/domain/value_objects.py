import attrs

from apps.users import models
from domain.base.value_objects import Entity


@attrs.define(slots=True)
class User(Entity):
    id: int
    email: int
    first_name: str
    last_name: str
    phone_number: int
    company: str

    @classmethod
    def from_model(cls, user: models.User) -> 'User':
        return cls(
            id=user.id,
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name,
            phone_number=user.phone_number,
            company=user.company,
        )


@attrs.define(slots=True)
class CreateUser(Entity):
    email: int
    first_name: str
    last_name: str
    phone_number: int
    company: str
    create_team: bool


@attrs.define(slots=True)
class CreateTeam(Entity):
    user_id: int
    team_name: str


@attrs.define(slots=True)
class Member(Entity):
    external_id: str
    first_name: str
    last_name: str

    @classmethod
    def from_model(cls, member: models.User):
        return cls(
            external_id=str(member.external_id),
            first_name=member.first_name,
            last_name=member.last_name,
        )


@attrs.define(slots=True)
class Team(Entity):
    team_name: str
    members: list[Member]

    @classmethod
    def from_model(cls, team: models.Team):
        return cls(
            team_name=team.team_name,
            members=[Member.from_model(member=member) for member in team.members.all()],
        )
