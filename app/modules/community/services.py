from core.services.BaseService import BaseService
from app.modules.community.models import Community
from app.modules.community.repositories import CommunityRepository

from app import db, community_members


class CommunityService(BaseService):
    def __init__(self):
        self.repository = CommunityRepository()
        super().__init__(self.repository)

    # Lista las comunidades dado un user
    def get_all_by_user(self, user):
        return self.repositry.get_all_by_user

    # Crea una comunidad y la asigna al usuario que la crea
    def create(self, name, description, user):
        community = Community(name=name, description=description)
        community.members.append(user)

        db.session.add(community)
        try:
            db.session.commit()
            return {"success": True, "community": community}
        except Exception as e:
            db.session.rollback()
            return {"success": False, "error": str(e)}

    # Comprueba si un usuario pertenece a una comunidad dada
    def is_member(self, community_id, user_id):
        return db.session.querry(community_members).filter_by(user_id=user_id,
                                                              community_id=community_id).first is not None
