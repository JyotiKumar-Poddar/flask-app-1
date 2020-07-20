import null as null
from flask import Flask, jsonify, abort, request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)
data = [
    {
        "id": 1,
        "employee_name": "Tiger Nixon",
        "employee_salary": "320800",
        "employee_age": "61",
        "profile_image": ""
    },
    {
        "id": 2,
        "employee_name": "Garrett Winters",
        "employee_salary": "170750",
        "employee_age": "63",
        "profile_image": ""
    },
    {
        "id": 3,
        "employee_name": "Ashton Cox",
        "employee_salary": "86000",
        "employee_age": "66",
        "profile_image": ""
    },
    {
        "id": 4,
        "employee_name": "Cedric Kelly",
        "employee_salary": "433060",
        "employee_age": "22",
        "profile_image": ""
    },
    {
        "id": 5,
        "employee_name": "Airi Satou",
        "employee_salary": "162700",
        "employee_age": "33",
        "profile_image": ""
    },
    {
        "id": 6,
        "employee_name": "Brielle Williamson",
        "employee_salary": "372000",
        "employee_age": "61",
        "profile_image": ""
    },
    {
        "id": 7,
        "employee_name": "Herrod Chandler",
        "employee_salary": "137500",
        "employee_age": "59",
        "profile_image": ""
    },
    {
        "id": 8,
        "employee_name": "Rhona Davidson",
        "employee_salary": "327900",
        "employee_age": "55",
        "profile_image": ""
    },
    {
        "id": 9,
        "employee_name": "Colleen Hurst",
        "employee_salary": "205500",
        "employee_age": "39",
        "profile_image": ""
    },
    {
        "id": 10,
        "employee_name": "Sonya Frost",
        "employee_salary": "103600",
        "employee_age": "23",
        "profile_image": ""
    },
    {
        "id": 11,
        "employee_name": "Jena Gaines",
        "employee_salary": "90560",
        "employee_age": "30",
        "profile_image": ""
    },
    {
        "id": 12,
        "employee_name": "Quinn Flynn",
        "employee_salary": "342000",
        "employee_age": "22",
        "profile_image": ""
    },
    {
        "id": 13,
        "employee_name": "Charde Marshall",
        "employee_salary": "470600",
        "employee_age": "36",
        "profile_image": ""
    },
    {
        "id": 14,
        "employee_name": "Haley Kennedy",
        "employee_salary": "313500",
        "employee_age": "43",
        "profile_image": ""
    },
    {
        "id": 15,
        "employee_name": "Tatyana Fitzpatrick",
        "employee_salary": "385750",
        "employee_age": "19",
        "profile_image": ""
    }
]


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/service/api/v1/employees', methods=['GET'])
def get_tasks():
    return jsonify({'data': data})


@app.route('/service/api/v1/employees/<int:emp_id>', methods=['GET'])
def get_task(emp_id):
    emp = null
    d =[]
    for val in data:
        if val['id'] == emp_id:
            emp = val
            break

    d.append(emp)
    return jsonify({'data': d})


@app.route('/service/api/v1/employees', methods=['POST'])
def create_task():
    print(" request.json   ============", request.json)
    if not request.json or not 'employee_name' in request.json:
        abort(400)

    s1 = {
        'id': request.json.get('id', ""),
        'employee_name': request.json.get('employee_name', ""),
        'employee_salary': request.json.get('employee_salary', ""),
        'employee_age': request.json.get('employee_age', ""),
        'employee_image': request.json.get('employee_image', "")

    }
    print("====== s1", s1)
    data.append(s1)
    return jsonify({'data': data}), 201


@app.route('/service/api/v1/employees/<int:emp_id>', methods=['DELETE'])
def delete_task(emp_id):
    d = []
    for val in data:
        if val['id'] == emp_id:
            emp = val
            break

    print("SIze before ", len(data))
    data.remove(val)
    print("SIze is ", len(data))
    return jsonify({'data': data})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090, debug=True)
    # app.run(debug=True)
