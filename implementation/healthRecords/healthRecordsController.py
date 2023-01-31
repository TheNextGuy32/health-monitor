from flask import Blueprint, request
from flask_cors import cross_origin

healthRecordsController = Blueprint('healthRecordsController',__name__)

from implementation.healthRecords import healthRecordsDynamoAccess

@healthRecordsController.route('/health-records', methods = ['GET'])
@cross_origin
def getHealthRecords():
    return { "healthRecords": healthRecordsDynamoAccess.getHealthRecords()}, 200

@healthRecordsController.route('/health-records', methods = ['POST'])
@cross_origin
def createHealthRecord():
    body = request.get_json()

    recordType = body.get("recordType")
    if recordType == None or recordType == "":
        message = "A recordType is required."
        return {'message': message}, 400

    healthRecordsDynamoAccess.createHealthRecord(recordType)
    return { "success": True }, 200
