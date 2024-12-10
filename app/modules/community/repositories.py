from core.repositories.BaseRepository import BaseRepository
from app.modules.community.models import Community
from app.modules.auth.models import User


class CommunityRepository(BaseRepository):
    def __init__(self):
        super().__init__(Community)

    def get_all_by_user(self, user):
        return self.model.query.join(self.model.members).filter(User.id == user).all()
