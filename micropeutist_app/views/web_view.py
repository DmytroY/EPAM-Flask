''' WEB controller '''
from flask import render_template, redirect, request, flash

from ..service.services import *
from ..config import app

# ========= DOCTORS ==========
@app.route('/')
@app.route('/doctors/')
def doctors():
    '''list of doctors'''
    data = get_doctors()
    return render_template("doctor_list.html", data=data)

@app.route('/new_doctor/', methods=['GET', 'POST'])
def new_doctor():
    '''add new doctor'''
    if request.method == "POST":
        data = {}
        data['first_name'] = request.form.get("first_name")
        data['last_name'] = request.form.get("last_name")
        data['grade'] = request.form.get("grade")
        data['specialization'] = request.form.get("specialization")
        data['email'] = request.form.get("email")
        feedback = create_doctor(data)
        if feedback == 'success':
            flash('New doctor record created!',  category='message')
        else:
            flash(feedback, category='error')
        return redirect("/")
    return render_template("new_doctor.html")

@app.route('/doctor/', methods=['GET'])
def doctor():
    '''Show a doctor data by id or by email '''
    doctor_id = request.args.get('id')
    print("=== doctor_id = ", doctor_id)
    doctor_list = receive_doctor(doctor_id)
    return render_template("doctor.html", data=doctor_list)

@app.route('/edit_doctor/', methods=['GET', 'POST'])
def edit_doctor():
    '''Edit doctor record'''
    # GET
    if request.method == "GET":
        id = request.args.get('id')
        print("=== edit doc id=", id)
        doctor = receive_doctor(id)
        return render_template("edit_doctor.html", data=doctor)
    # POST
    data = {}
    data['id'] = request.form.get("id")
    data['first_name'] = request.form.get("first_name")
    data['last_name'] = request.form.get("last_name")
    data['grade'] = request.form.get("grade")
    data['specialization'] = request.form.get("specialization")
    data['email'] = request.form.get("email")
    feedback = update_doctor(data)
    if feedback == 'success':
        flash('Doctor record updated!',  category='message')
    else:
        flash(feedback, category='error')
    return redirect("/")

@app.route('/remove_doctor/', methods=['GET'])
def remove_doctor():
    id = request.args.get('id')
    feedback = delete_doctor(id)
    if feedback == 'success':
        flash('Doctor record deleted!',  category='message')
    else:
        flash(feedback, category='error')
    return redirect("/")

# ========= PATIENTS =======
@app.route('/patients/', methods=['GET', 'POST'])
def patients():
    '''list of patients with search block'''
    if request.method == "GET":
        return render_template("patient_list.html", patients=get_patients(), doctors=get_doctors())
    # POST
    search_criterias = {}
    search_criterias['birthday_since'] = (request.form.get("birthday_since") or "0001-01-01")
    search_criterias['birthday_till'] = (request.form.get("birthday_till") or "9999-12-31")
    search_criterias['doctor_id'] = request.form.get("doctor_id")
    print("=== search criterias: ",  search_criterias)
    return render_template("patient_list.html",
                           patients=get_patients(**search_criterias),
                           doctors=get_doctors())

@app.route('/new_patient/', methods=['GET', 'POST'])
def new_patient():
    if request.method == "GET":
        doctor_id = request.args.get('doctor_id')
        if doctor_id:
            doctor = receive_doctor(doctor_id)
            return render_template('new_patient.html', doctor=doctor)
        return redirect('/')
    
    data = {}
    data['first_name'] = request.form.get("first_name")
    data['last_name'] = request.form.get("last_name")
    data['gender'] = request.form.get("gender")
    data['birthday'] = request.form.get("birthday")
    data['health_state'] = request.form.get("health_state")
    data['email'] = request.form.get("email")
    data['doctor_id'] = int(request.form.get("doctor_id"))
    print("==== new patient data:", data)
    feedback = create_patient(data)
    if feedback == 'success':
        flash('New patient created!',  category='message')
    else:
        flash(feedback, category='error')
    print("=== redirect to: /doctor/?id=" + str(data['doctor_id']))
    return redirect("/doctor/?id=" + str(data['doctor_id']))

@app.route('/patient/', methods=['GET'])
def patient():
    '''Show a patient data by id or by email'''
    id = request.args.get('id')
    patient_list = receive_patient(id)
    return render_template("patient.html", data=patient_list)

@app.route('/edit_patient/', methods=['GET', 'POST'])
def edit_patient():
    ''' edit patient '''
    if request.method == "GET":
        id = request.args.get('id')
        return render_template("edit_patient.html", data=receive_patient(id), doctors=get_doctors())
    # POST
    data = {}
    data['id'] = request.form.get("id")
    data['first_name'] = request.form.get("first_name")
    data['last_name'] = request.form.get("last_name")
    data['gender'] = request.form.get("gender")
    data['birthday'] = request.form.get("birthday")
    data['health_state'] = request.form.get("health_state")    
    data['email'] = request.form.get("email")
    data['doctor_id'] = request.form.get("doctor_id")
    feedback = update_patient(data)
    if feedback == 'success':
        flash('Patient record updated!',  category='message')
    else:
        flash(feedback, category='error')
    return redirect("/patients")

@app.route('/remove_patient/', methods=['GET'])
def remove_patient():
    ''' deleting patiend by id'''
    id = request.args.get('id')
    feedback = delete_patient(id)
    if feedback == "success":
        flash('Patient record deleted', category='message')
    else:
        flash(feedback, category='error')
    return redirect('/patients')

