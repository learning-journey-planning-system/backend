class Person(db.Model):
    __tablename__ = 'person'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    title = db.Column(db.String(10))

    __mapper_args__ = {
        'polymorphic_identity': 'person'
    }

    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result


class Doctor(Person):
    __tablename__ = 'doctor'

    id = db.Column(db.Integer, db.ForeignKey('person.id'), primary_key=True)
    reg_num = db.Column(db.String(15))
    hourly_rate = db.Column(db.Integer)

    __mapper_args__ = {
        'polymorphic_identity': 'doctor',
    }

    def calculate_charges(self, num_mins):
        """
        Uses the doctor's hourly rate to determine how much
        a 'num_mins' length appointment should be charged.
        NB: an appointment shorter than 10 mins is charged
        as if it were 10 mins long.
        """
        if num_mins < 10:
            result = self.hourly_rate / 6
        else:
            result = self.hourly_rate * (num_mins / 60)
        return result


class Patient(Person):
    __tablename__ = 'patient'

    id = db.Column(db.Integer, db.ForeignKey('person.id'), primary_key=True)
    contact_num = db.Column(db.String(15))
    ewallet_balance = db.Column(db.Integer, default=0)

    __mapper_args__ = {
        'polymorphic_identity': 'patient',
    }

    def ewallet_topup(self, amount):
        """
        Tops up a patient's e-wallet account.
        'amount' must be positive.
        """
        if amount >= 0:
            self.ewallet_balance += amount
        else:
            raise Exception("Negative topups not allowed.")

    def ewallet_withdraw(self, amount):
        """
        Withdraws an 'amount' from the patient's e-wallet if
        there is sufficient balance.
        """
        if self.ewallet_balance >= amount:
            self.ewallet_balance -= amount
        else:
            raise Exception("Unable to withdraw: insufficient balance.")


class Consultation(db.Model):
    __tablename__ = 'consultation'

    id = db.Column(db.Integer, primary_key=True)
    diagnosis = db.Column(db.String(100))
    prescription = db.Column(db.String(30))
    charge = db.Column(db.Integer)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'))
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'))

    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result