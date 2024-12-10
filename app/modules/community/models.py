from app import db


class Community(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    members = db.relationship('Users', secondary='members', back_populates='communities')

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()
