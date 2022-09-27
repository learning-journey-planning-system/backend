@app.route("/persons/<int:person_id>")
def person_by_id(person_id):
    person = Person.query.filter_by(id=person_id).first()
    if person:
        return jsonify({
            "data": person.to_dict()
        }), 200
    else:
        return jsonify({
            "message": "Person not found."
        }), 404


@app.route("/doctors")
def doctors():
    search_name = request.args.get('name')
    if search_name:
        doctor_list = Doctor.query.filter(Doctor.name.contains(search_name))
    else:
        doctor_list = Doctor.query.all()
    return jsonify(
        {
            "data": [doctor.to_dict() for doctor in doctor_list]
        }
    ), 200


@app.route("/doctors", methods=['POST'])
def create_doctor():
    data = request.get_json()
    if not all(key in data.keys() for
               key in ('name', 'title',
                       'reg_num', 'hourly_rate')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500
    doctor = Doctor(**data)
    try:
        db.session.add(doctor)
        db.session.commit()
        return jsonify(doctor.to_dict()), 201
    except Exception:
        return jsonify({
            "message": "Unable to commit to database."
        }), 500


@app.route("/patients")
def patients():
    search_name = request.args.get('name')
    if search_name:
        patient_list = Patient.query.filter(Doctor.name.contains(search_name))
    else:
        patient_list = Patient.query.all()
    return jsonify(
        {
            "data": [patient.to_dict() for patient in patient_list]
        }
    ), 200


@app.route("/patients", methods=['POST'])
def create_patient():
    data = request.get_json()
    if not all(key in data.keys() for
               key in ('name', 'title',
                       'contact_num', 'ewallet_balance')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500
    patient = Patient(**data)
    try:
        db.session.add(patient)
        db.session.commit()
        return jsonify(patient.to_dict()), 201
    except Exception:
        return jsonify({
            "message": "Unable to commit to database."
        }), 500


@app.route("/consultations")
def consultations():
    consultation_list = Consultation.query.all()
    return jsonify(
        {
            "data": [consultation.to_dict()
                     for consultation in consultation_list]
        }
    ), 200


@app.route("/consultations", methods=['POST'])
def create_consultation():
    data = request.get_json()
    if not all(key in data.keys() for
               key in ('doctor_id', 'patient_id',
                       'diagnosis', 'prescription', 'length')):
        return jsonify({
            "message": "Incorrect JSON object provided."
        }), 500

    # (1): Validate doctor
    doctor = Doctor.query.filter_by(id=data['doctor_id']).first()
    if not doctor:
        return jsonify({
            "message": "Doctor not valid."
        }), 500

    # (2): Compute charges
    charge = doctor.calculate_charges(data['length'])

    # (3): Validate patient
    patient = Patient.query.filter_by(id=data['patient_id']).first()
    if not patient:
        return jsonify({
            "message": "Patient not valid."
        }), 500

    # (4): Subtract charges from patient's e-wallet
    try:
        patient.ewallet_withdraw(charge)
    except Exception:
        return jsonify({
            "message": "Patient does not have enough e-wallet funds."
        }), 500

    # (4): Create consultation record
    consultation = Consultation(
        diagnosis=data['diagnosis'], prescription=data['prescription'],
        doctor_id=data['doctor_id'], patient_id=data['patient_id'],
        charge=charge
    )

    # (5): Commit to DB
    try:
        db.session.add(consultation)
        db.session.commit()
        return jsonify(consultation.to_dict()), 201
    except Exception:
        return jsonify({
            "message": "Unable to commit to database."
        }), 500