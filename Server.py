from flask import Flask, request, jsonify
import statistics

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate_weather_stats():
    try:
        data = request.get_json()
        temperatures = data.get('temperatures', [])
        
        if len(temperatures) != 5:
            return jsonify({'error': 'Need exactly 5 temperatures'}), 400
        
        result = {
            'average': statistics.mean(temperatures),
            'minimum': min(temperatures),
            'maximum': max(temperatures),
            'status': 'success'
        }
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)