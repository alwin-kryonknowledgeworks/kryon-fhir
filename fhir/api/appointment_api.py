from flask import request, jsonify
from fhir import app, clustor


@app.route('/appointment',methods=['POST'])
def appointment():
    data = request.json
    resource=data["resourceType"]
    get_id=data["id"]
    appointment=clustor[resource]
    results=appointment.find()
    id_store=[]
    for id in results:
        id_store.append(id.get("id"))
    if get_id not in id_store:
        appointment.insert_one(data)
        return jsonify({"message": "Created Appointment"}),201

    else:
        return jsonify({"Error": "Appointment is already registered"}),400


from bson import json_util, ObjectId
import json

@app.route('/appointment',methods=["GET"])
def appointment_get():
    data=request.args.get('id')
    appointment = clustor["Appointment"]
    appointment_list = appointment.find({"id": int(data)})
    for resource in appointment_list:
        del resource['_id']
        page_sanitized = json.loads(json_util.dumps(resource))
        return jsonify({"result": page_sanitized}), 200
    return jsonify({"Error":"No Appointment"}) ,400

@app.route('/appointment',methods=["PUT"])
def appointment_update():
    data = request.json
    id =data["id"]
    appointment=clustor["Appointment"]
    appointment.find_one_and_update({"id": int(id)},{"$set": data})
    return jsonify({"message": "Updated Appointment"}), 200

@app.route('/appointment',methods=["DELETE"])
def appointment_delete():
    data= request.args.get("id")
    clustor["Appointment"].find_one_and_delete({"id": int(data)})
    return jsonify({"message": "Delete Appointment"}), 200