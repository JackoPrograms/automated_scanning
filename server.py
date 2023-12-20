from flask import Flask, request, send_from_directory
import os

app = Flask(__name__, static_folder='static')

@app.route('/', methods=['GET'])
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/create_domain_file', methods=['POST'])
def create_domain_file():
    text = request.data.decode('utf-8')
    with open('./automated_scanning/domain_name.txt', 'w') as file:
        file.write(text)
    return 'Domain name saved'

@app.route('/create_tags_file', methods=['POST'])
def create_tags_file():
    tags = request.data.decode('utf-8')
    with open('./automated_scanning/tags_vulnerabilities.txt', 'w') as file:
        file.write(tags)
    return 'Tags saved'

@app.route('/create_severity_file', methods=['POST'])
def create_severity_file():
    severity = request.data.decode('utf-8')
    with open('./automated_scanning/severity_vulnerabilities.txt', 'w') as file:
        file.write(severity)
    return 'Severity saved'

# @app.route('/start_scan', methods=['GET'])
# def start_scan():
    # os.system('start_scan_target.bat')
    # return 'Scan started'

@app.route('/start_scan_command', methods=['POST'])
def start_scan_command():
    try:
        # Предполагается, что start_scan_target.bat находится в той же папке, что и server.py
        os.system('start_scan_target.bat')
        return 'Scan started'
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run()