import uuid
from flask import Flask, json, request

api = Flask(__name__)

stats = [
            {
                "jobid": 1, 
                "name": "Job 1",
                "count": 10,
                "cities": [
                    {
                        "name": "Novi Sad",
                        "count": 4
                    },
                    {
                        "name": "Beograd",
                        "count": 3
                    },
                    {
                        "name": "Bačka Palanka",
                        "count": 3
                    }
                ],
                "submissions": [
                    {"start":"0am", "end":"3am", "count": 2},
                    {"start":"9am", "end":"12am", "count": 2},
                    {"start":"6pm", "end":"9pm", "count": 5},
                    {"start":"9pm", "end":"0am", "count": 1}
                ]
            },
            {
                "jobid": 2, 
                "name": "Job 2",
                "count": 1,
                "cities": [
                    {
                        "name": "Novi Sad",
                        "count": 1,
                    }
                ],
                "submissions": [
                    {"start":"10pm", "end":"11pm", "count": 1}
                ]
            }
        ]

@api.route('/api/job-stats', methods=['GET'])
def send_stats():
    return json.dumps(stats), 200, {'Content-Type': 'application/json; charset=utf-8', 'Access-Control-Allow-Origin': '*'}


@api.route('/api/pay-conference', methods=['POST'])
def pay_conference():
    pay_for_service(request.data)
    return "", 204, {'Access-Control-Allow-Origin': '*'}

@api.route('/api/pay-accomodation', methods=['POST'])
def pay_accomodation():
    pay_for_service(request.data)
    return "", 204, {'Access-Control-Allow-Origin': '*'}

@api.route('/api/pay-transportation', methods=['POST'])
def pay_transportation():
    pay_for_service(request.data)
    return "", 204, {'Access-Control-Allow-Origin': '*'}

@api.route('/api/job-application', methods=['POST'])
def job_application():
    print("Received Job Application indexing unit: " + str(request.data))
    return "", 204, {'Access-Control-Allow-Origin': '*'}

@api.route('/api/cv', methods=['PUT'])
def put_cv():
    name = save_pdf_with_random_name(request.data)
    print("Received CV file for Job Application for User with userId: " + str(request.headers['candidateId']) + ". File saved in ./temp/" + name)
    return "", 204, {'Access-Control-Allow-Origin': '*'}

@api.route('/api/invoice', methods=['PUT'])
def put_invoice():
    name = save_pdf_with_random_name(request.data)
    print("File (invoice) saved in ./temp/" + name)
    return "", 204, {'Access-Control-Allow-Origin': '*'}

def pay_for_service(data):
    print("Payment request:" + str(data))

def save_pdf_with_random_name(data):
    name = str(uuid.uuid4()) + ".pdf"
    with open('./temp/' + name, 'wb') as f:
        f.write(data)
        f.close()
    return name

if __name__ == '__main__':
    api.run(debug=True, port=81) 