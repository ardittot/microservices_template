from flask_sqlalchemy import SQLAlchemy

# initialize sql-alchemy
db = SQLAlchemy()

class Bucketlist(db.Model):
    """This class represents the bucketlist table."""

    __table_args__ = {"schema": "cashman"}
    __tablename__ = "bucketlists"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    date_created  = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def __init__(self, name):
        """initialize with name."""
        self.name = name

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Bucketlist.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<Bucketlist: {}>".format(self.name)

class Ex1(db.Model):
    __table_args__ = {"schema": "cashman"}
    __tablename__ = "ex1"
    id = db.Column(db.BigInteger, primary_key=True, unique=True)
    amount = db.Column(db.BigInteger)
    description = db.Column(db.VARCHAR(20))

    def __init__(self, id, amount, description):
        self.id = id
        self.amount = amount
        self.description = description

    def __repr__(self):
        return '<Ex1 %d %d %s>' % (self.id, self.amount, self.description)

class TestEForm(db.Model):

    __table_args__ = {"schema": "cashman"}
    __tablename__ = "testeform"

    id = db.Column(db.BigInteger, primary_key=True)
    ## Customized columns ##
    Nama_Lengkap = db.Column(db.String(255))
    Jenis_Kelamin = db.Column(db.String(8))
    No_Identitas = db.Column(db.String(32))
    Nama_Uker = db.Column(db.String(32))
    ########################
    date_created  = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def __init__(self, Nama_Lengkap, Jenis_Kelamin, No_Identitas, Nama_Uker):
        """initialize with name."""
        self.Nama_Lengkap = Nama_Lengkap
        self.Jenis_Kelamin = Jenis_Kelamin
        self.No_Identitas = No_Identitas
        self.Nama_Uker = Nama_Uker

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return TestEForm.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<TestEForm: {} {} {} {}>".format(self.Nama_Lengkap, self.Jenis_Kelamin, self.No_Identitas, self.Nama_Uker)
