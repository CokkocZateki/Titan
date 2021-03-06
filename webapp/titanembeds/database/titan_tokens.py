from titanembeds.database import db

class TitanTokens(db.Model):
    __tablename__ = "titan_tokens"
    id = db.Column(db.Integer, primary_key=True)                    # Auto increment id
    user_id = db.Column(db.String(255), nullable=False)             # Discord user id of user
    tokens = db.Column(db.Integer, nullable=False, default=0)       # Token amount
    
    def __init__(self, user_id, tokens):
        self.user_id = user_id
        self.tokens = tokens

def get_titan_token(user_id):
    q = db.session.query(TitanTokens).filter(TitanTokens.user_id == user_id).first()
    if q:
        return q.tokens
    else:
        return -1