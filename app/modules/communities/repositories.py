from app.modules.communities.models import Communities
from core.repositories.BaseRepository import BaseRepository


class CommunitiesRepository(BaseRepository):
    def __init__(self):
        super().__init__(Communities)
