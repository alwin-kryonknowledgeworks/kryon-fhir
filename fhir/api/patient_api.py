from flask import request, jsonify
from fhir import app, clustor

@app.route('/patient',methods=['POST'])
def patient():
    data = request.json
    resource=data["resourceType"]
    get_id=data["id"]
    patient=clustor[resource]
    results=patient.find()
    id_store=[]
    for id in results:
        id_store.append(id.get("id"))
    if get_id not in id_store:
        patient.insert_one(data)
        return jsonify({"message": "Created Patient"}),201

    else: 
        return jsonify({"Error": "Patient is already registered"}),401

from bson import json_util, ObjectId
import json

@app.route('/patient',methods=["GET"])
def patient_get():
    data=request.args.get('id')
    patients = clustor["Patient"]
    patient=patients.find({"id": int(data)})
    for resource in patient:
        del resource['_id']
        page_sanitized = json.loads(json_util.dumps(resource))
        return jsonify({"result": page_sanitized}), 200
    return jsonify({"Error": "No Patient ID"})


@app.route('/patient',methods=["PUT"])
def patient_update():
    data = request.json
    id =data["id"]
    patients=clustor["Patient"]
    patients.find_one_and_update({"id": int(id)},{"$set": data})
    return jsonify({"message": "Updated Patient"}), 200


@app.route('/patient',methods=["DELETE"])
def patient_delete():
    data= request.args.get("id")
    clustor["Patient"].find_one_and_delete({"id": int(data)})
    return jsonify({"message": "Delete Patient"}), 200