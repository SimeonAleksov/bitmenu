from apps.users.domain import repositories
from apps.users.domain import value_objects


class UserService:
    @classmethod
    def create(cls, **kwargs):
        user = repositories.UserRepository.create(entity=value_objects.CreateUser(kwargs))
        repositories.TeamRepository.create(
            entity=value_objects.CreateTeam(
                user_id=user.id,
                team_name=user.company,
            )
        )
