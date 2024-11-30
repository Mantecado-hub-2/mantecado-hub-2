from app.modules.communities.repositories import CommunitiesRepository
from core.services.BaseService import BaseService


class CommunitiesService(BaseService):
    def __init__(self):
        super().__init__(CommunitiesRepository())
