from app import db


class Communities(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return f'Communities<{self.id}>'
