from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_demo_data():
    # Data based on provided table
    DATA = [
        {"timestamp": "2023-10-25 12:00:00", "token": 1234567, "underlying": "NIFTY", "underlying_price": 19133.05, "strike": 19100, "strike_price": 180.05, "type": "c", "days_to_expiry": 9},
        {"timestamp": "2023-10-25 12:00:00", "token": 1234567, "underlying": "NIFTY", "underlying_price": 19133.05, "strike": 19100, "strike_price": 130.35, "type": "p", "days_to_expiry": 9},
        {"timestamp": "2023-10-25 12:00:00", "token": 1234567, "underlying": "NIFTY", "underlying_price": 19133.05, "strike": 19000, "strike_price": 245.45, "type": "c", "days_to_expiry": 9},
        {"timestamp": "2023-10-25 12:00:00", "token": 1234567, "underlying": "NIFTY", "underlying_price": 19133.05, "strike": 19000, "strike_price": 93.9, "type": "p", "days_to_expiry": 9},
        {"timestamp": "2023-10-25 12:00:00", "token": 1234567, "underlying": "NIFTY", "underlying_price": 19133.05, "strike": 19200, "strike_price": 127.1, "type": "c", "days_to_expiry": 9},
        {"timestamp": "2023-10-25 12:00:00", "token": 1234567, "underlying": "NIFTY", "underlying_price": 19133.05, "strike": 19200, "strike_price": 176, "type": "p", "days_to_expiry": 9},
        {"timestamp": "2023-10-25 12:00:00", "token": 1234567, "underlying": "NIFTY", "underlying_price": 19133.05, "strike": 19300, "strike_price": 84.5, "type": "c", "days_to_expiry": 9},
        {"timestamp": "2023-10-25 12:00:00", "token": 1234567, "underlying": "NIFTY", "underlying_price": 19133.05, "strike": 19050, "strike_price": 110.5, "type": "p", "days_to_expiry": 9},
        {"timestamp": "2023-10-25 12:00:00", "token": 1234567, "underlying": "NIFTY", "underlying_price": 19133.05, "strike": 19400, "strike_price": 53.25, "type": "c", "days_to_expiry": 9},
        {"timestamp": "2023-10-25 12:00:00", "token": 1234567, "underlying": "NIFTY", "underlying_price": 19133.05, "strike": 18900, "strike_price": 66.45, "type": "p", "days_to_expiry": 9},
    ]

    return jsonify(DATA), 200

if __name__ == "__main__":
     app.run(debug=True, port=5001)
