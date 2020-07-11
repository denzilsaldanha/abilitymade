from flask import Flask, render_template, request
import json

app = Flask(__name__)


class Orthotist:
    def __init__(self, **Orthotist):
        self.practiceName = Orthotist['practiceName']
        self.practiceAddress = Orthotist['practiceAddress']
        self.practicePh = Orthotist['practicePh']
        self.orthotistName = Orthotist['orthotistName']


# List of Orthotists
orthotistsList = [Orthotist(**{'practiceName': 'P1',
                               'practiceAddress': 'Kensington',
                               'practicePh': '0401254789',
                               'orthotistName': 'o1'}),
                  Orthotist(**{'practiceName': 'P2',
                               'practiceAddress': 'Mascot',
                               'practicePh': '0408795478',
                               'orthotistName': 'o2'}, ),
                  Orthotist(**{'practiceName': 'P3',
                               'practiceAddress': 'Randwick',
                               'practicePh': '0401254129',
                               'orthotistName': 'o3'}),
                  Orthotist(**{'practiceName': 'P4',
                               'practiceAddress': 'Botany',
                               'practicePh': '0408987789',
                               'orthotistName': 'o4'}),
                  Orthotist(**{'practiceName': 'P5',
                               'practiceAddress': 'Glenfield',
                               'practicePh': '0401212389',
                               'orthotistName': 'o5'})
                  ]


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/orthotist', methods =["GET"])
def orthotist():
    if request.method == 'GET':
        orthotistJson = []
        for obj in orthotistsList:
            orthotistJson.append(obj.__dict__)
        return json.dumps(orthotistJson)
@app.route('/js/script.js', methods = ['GET'])
def javascript():
    if request.method =='GET':
        return render_template('/js/script.js')

@app.route('/patient', methods=['POST', 'GET'])
def patient():
    if request.method == 'GET':
        return render_template('patient.html')

patientList = []

@app.route('/patient/details', methods=['POST', 'GET'])
def patientdetails():
    if request.method == 'GET':
        list_patient = []
        for obj in patientList:
            list_patient.append(obj.__dict__)
            # print(list_orders)
        return json.dumps(list_patient)
    if request.method == 'POST':
        patient_details = request.json
        print(patient_details)
        patientList.append(Patient(**patient_details))
        return '200 OK'

if __name__ == '__main__':
    app.run(debug=True)
