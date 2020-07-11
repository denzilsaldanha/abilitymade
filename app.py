from flask import Flask, render_template
import json

app = Flask(__name__)

class Orthotist:
    def __init__(self, **Orthotist):
        self.practiceName = Orthotist['practiceName']
        self.practiceAddress = Orthotist['practiceAddress']
        self.practicePh = Orthotist['practicePh']
        self.orthotistName = Orthotist['orthotistName']

#List of Orthotists
orthotistsList = [Orthotist(**{'practiceName':'P1',
                             'practiceAddress':'Kensington',
                             'practicePh':'0401254789',
                             'orthotistName':'o1'}),
                  Orthotist(**{'practiceName': 'P2',
                               'practiceAddress': 'Mascot',
                               'practicePh': '0408795478',
                               'orthotistName': 'o2'},),
                  Orthotist(**{'practiceName':'P3',
                             'practiceAddress':'Randwick',
                             'practicePh':'0401254129',
                             'orthotistName':'o3'}),
                  Orthotist(**{'practiceName':'P4',
                             'practiceAddress':'Botany',
                             'practicePh':'0408987789',
                             'orthotistName':'o4'}),
                  Orthotist(**{'practiceName':'P5',
                             'practiceAddress':'Glenfield',
                             'practicePh':'0401212389',
                             'orthotistName':'o5'})
                  ]
for obj in orthotistsList:
    print(obj.__dict__)