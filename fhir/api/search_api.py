from flask import request, jsonify
from flask_jwt_extended import jwt_required
from fhir import app, fhir_collection


@app.route('/api/v1/search', methods=['GET'])
@jwt_required()
def find():
    resource = request.args.get("resource_type")
    if not resource:
        return jsonify({'return': "error"}), 401
    pipeline = [
        {
            "$match":
                {"resource_type": {"$regex": f"^{resource}", '$options': 'i'}}
        }
    ]
    results = fhir_collection.aggregate(pipeline)
    list_group = list(results)
    for i in list_group:
        del i['_id']

    return jsonify({'result': list_group}), 200


