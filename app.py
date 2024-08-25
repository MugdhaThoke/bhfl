from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def process_data():
    data = request.json.get('data', [])
    numbers = [item for item in data if item.isdigit()]
    alphabets = [item for item in data if item.isalpha()]
    highest_lowercase = sorted([ch for ch in alphabets if ch.islower()], reverse=True)

    response = {
        "is_success": True,
        "user_id": "Mugdha_Thoke_09092003",  
        "email": "mugdhathoke0909@gmail.com",  
        "roll_number": "21BCT0194",  
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": highest_lowercase[:1] if highest_lowercase else []
    }
    return jsonify(response)


@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    return jsonify({"operation_code": 1}), 200

if __name__ == '__main__':
    app.run(debug=True)
