###  Вариант 6

# from flask import Flask, request, send_file

# app = Flask(__name__)

# @app.route('/', methods=['GET'])
# def index():
#     return '''
#     <html>
#     <head>
#     <title>Button Example</title>
#     </head>
#     <body>
#     <input type="text" id="textInput">
#     <input type="checkbox" id="checkbox1">Checkbox 1
#     <input type="checkbox" id="checkbox2">Checkbox 2
#     <input type="checkbox" id="checkbox3">Checkbox 3
#     <button onclick="start()">Start</button>
#     <script src="script.js"></script>
#     </body>
#     </html>
#     '''

# @app.route('/start', methods=['POST'])
# def start():
#     text_input = request.form.get('text')
#     checkbox1 = request.form.get('checkbox1')
#     checkbox2 = request.form.get('checkbox2')
#     checkbox3 = request.form.get('checkbox3')
    
#     if checkbox1:
#         tags_vulnerabilities = 'vulnerability1'
#     else:
#         tags_vulnerabilities = ''
    
#     if checkbox2:
#         tags_vulnerabilities += 'vulnerability2'
    
#     if checkbox3:
#         tags_vulnerabilities += 'vulnerability3'
    
#     with open('domain_name.txt', 'w') as file:
#         file.write(text_input)
    
#     with open('tags_vulnerabilities.txt', 'w') as file:
#         file.write(tags_vulnerabilities)

#     return send_file('domain_name.txt', as_attachment=True, attachment_filename='domain_name.txt')

# if __name__ == '__main__':
#     app.run()








##  Сохраняет но выдаёт ошибку

# from flask import Flask, request, send_file
# import os

# app = Flask(__name__)

# # @app.route('/')
# @app.route('/', methods=['GET'])
# def index():
#     return '''
#     <html>
#     <head>
#       <title>Website</title>
#     </head>
#     <body>
#       <h1>Website</h1>
#       <form action="/create_files" method="POST">
#         <label for="inputText">Text:</label>
#         <input type="text" id="inputText" name="text"><br><br>
#         <input type="checkbox" id="checkpoint1" name="checkpoint1">
#         <label for="checkpoint1">Checkpoint 1</label><br>
#         <input type="checkbox" id="checkpoint2" name="checkpoint2">
#         <label for="checkpoint2">Checkpoint 2</label><br>
#         <input type="checkbox" id="checkpoint3" name="checkpoint3">
#         <label for="checkpoint3">Checkpoint 3</label><br><br>
#         <input type="submit" value="Start">
#       </form>
#     </body>
#     </html>
#     '''

# @app.route('/create_file', methods=['POST'])
# def create_file():
#     text = request.form['text']
#     checkboxes = request.form.getlist('checkbox')
    
#     with open('domain_name.txt', 'w') as file:
#         file.write(text)

#     tags_vulnerabilities = []
#     for cb in checkboxes:
#         if cb == 'checkbox1':
#             tags_vulnerabilities.append('vulnerability1')
#         elif cb == 'checkbox2':
#             tags_vulnerabilities.append('vulnerability2')
#         elif cb == 'checkbox3':
#             tags_vulnerabilities.append('vulnerability3')

#     with open('tags_vulnerabilities.txt', 'w') as file:
#         file.write(''.join(tags_vulnerabilities))

#     return send_file('domain_name.txt', as_attachment=True, attachment_filename='domain_name.txt')


# if __name__ == '__main__':
#     app.run()







###   Не сохраняет но НЕ выдаёт ошибку

# from flask import Flask, request, send_file
# import os

# app = Flask(__name__)

# @app.route('/', methods=['GET'])
# def index():
#     return '''
#     <html>
#     <head>
#       <title>File Creation</title>
#       <script src="script.js"></script>
#     </head>
#     <body>
#       <h1>File Creation</h1>
#       <form>
#         <input type="text" id="text" name="text" placeholder="Enter Text">
#         <br><br>
#         <label for="checkbox1"><input type="checkbox" id="checkbox1" name="checkbox1"> Checkbox 1</label>
#         <br>
#         <label for="checkbox2"><input type="checkbox" id="checkbox2" name="checkbox2"> Checkbox 2</label>
#         <br>
#         <label for="checkbox3"><input type="checkbox" id="checkbox3" name="checkbox3"> Checkbox 3</label>
#         <br><br>
#         <button onclick="saveFile()">Start</button>
#       </form>
#     </body>
#     </html>
#     '''

# @app.route('/create_file', methods=['POST'])
# def create_file():
#     text = request.form['text']
#     checkboxes = request.form.getlist('checkbox')
    
#     with open('domain_name.txt', 'w') as file:
#         file.write(text)

#     tags_vulnerabilities = []
#     for cb in checkboxes:
#         if cb == 'checkbox1':
#             tags_vulnerabilities.append('vulnerability1')
#         elif cb == 'checkbox2':
#             tags_vulnerabilities.append('vulnerability2')
#         elif cb == 'checkbox3':
#             tags_vulnerabilities.append('vulnerability3')

#     with open('tags_vulnerabilities.txt', 'w') as file:
#         file.write(''.join(tags_vulnerabilities))

#     return send_file('domain_name.txt', as_attachment=True, attachment_filename='domain_name.txt')

# if __name__ == '__main__':
#     app.run()






# from flask import Flask, request, send_file
# import os

# app = Flask(__name__)

# # @app.route('/')
# @app.route('/', methods=['GET'])
# def index():
#     return '''
#     <html>
#         <body>
#             <h2>Введите текст:</h2>
#             <input type="text" id="text_input">
#             <br><br>
#             <input type="checkbox" id="checkbox1" value="vulnerability1"> Vulnerability 1
#             <br>
#             <input type="checkbox" id="checkbox2" value="vulnerability2"> Vulnerability 2
#             <br>
#             <input type="checkbox" id="checkbox3" value="vulnerability3"> Vulnerability 3
#             <br><br>
#             <button onclick="start()">Старт</button>
#         </body>
#         <script src="script.js"></script>
#     </html>
#     '''

# @app.route('/create_files', methods=['POST'])
# def create_files():
#     text_input = request.form.get('text_input')
#     checkbox1 = request.form.get('checkbox1')
#     checkbox2 = request.form.get('checkbox2')
#     checkbox3 = request.form.get('checkbox3')

#     with open('domain_name.txt', 'w') as file:
#         file.write(text_input)

#     tags_vulnerabilities = ''
#     if checkbox1 == 'on':
#         tags_vulnerabilities += 'vulnerability1'
#     if checkbox2 == 'on':
#         tags_vulnerabilities += 'vulnerability2'
#     if checkbox3 == 'on':
#         tags_vulnerabilities += 'vulnerability3'

#     with open('tags_vulnerabilities.txt', 'w') as file:
#         file.write(tags_vulnerabilities)

#     return send_file('domain_name.txt', as_attachment=True, attachment_filename='domain_name.txt')

# if __name__ == '__main__':
#     app.run()












# from flask import Flask, request, send_file

# app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     return '''
#     <html>
#     <body>
#         <form action="/create_files" method="post">
#             <input type="text" name="text" placeholder="Enter text" /><br>
#             <input type="checkbox" name="checkpoint1" value="Checkpoint 1" />Checkpoint 1<br>
#             <input type="checkbox" name="checkpoint2" value="Checkpoint 2" />Checkpoint 2<br>
#             <input type="submit" value="Create Text File" />
#         </form>
#     </body>
#     </html>
# '''

# @app.route('/create_files', methods=['POST'])
# def create_files():
#     text = request.form['text']
#     checkpoint1 = request.form.get('checkpoint1')
#     checkpoint2 = request.form.get('checkpoint2')
    
#     with open('domin_name.txt', 'w') as file:
#         file.write(text)
    
#     tags_vulnerabilities = ''
#     if checkpoint1:
#         tags_vulnerabilities += 'Checkpoint1'
#     if checkpoint2:
#         tags_vulnerabilities += 'Checkpoint2'
    
#     with open('tags_vulnerabilities.txt', 'w') as file:
#         file.write(tags_vulnerabilities)
    
#     return send_file('domin_name.txt', as_attachment=True, attachment_filename='domin_name.txt')

# if __name__ == '__main__':
#     app.run()








































###  Вариант 4

# from flask import Flask, request, send_file

# app = Flask(__name__)

# @app.route('/', methods=['GET'])
# def index():
#     return '''
#     <html>
#     <head>
#       <title>Button Example</title>
#       <script>
#         function createFile() {
#           var xhr = new XMLHttpRequest();
#           xhr.open('POST', '/create_file', true);
#           xhr.send();
#         }
#       </script>
#     </head>
#     <body>
#       <button onclick="createFile()">Create Text File</button>
#     </body>
#     </html>
#     '''

# @app.route('/create_file', methods=['POST'])
# def create_file():
#     with open('comand.txt', 'w') as file:
#         file.write('33333')

#     return send_file('comand.txt', as_attachment=True, attachment_filename='comand.txt')

# if __name__ == '__main__':
#     app.run()






###  Вариант 7

# from flask import Flask, request, send_file

# app = Flask(__name__)

# @app.route('/', methods=['GET'])
# def index():
#     return '''
#     <html>
#     <head>
#       <title>Button Example</title>
#       <script>
#         function createFile() {
#           var userInput = document.getElementById('userInput').value;
#           var xhr = new XMLHttpRequest();
#           xhr.open('POST', '/create_file', true);
#           xhr.setRequestHeader('Content-Type', 'text/plain');
#           xhr.send(userInput);
#         }
#       </script>
#     </head>
#     <body>
#       <input type="text" id="userInput">
#       <button onclick="createFile()">Create Text File</button>
#     </body>
#     </html>
#     '''

# @app.route('/create_file', methods=['POST'])
# def create_file():
#     text = request.data.decode('utf-8')
#     with open('domin_name.txt', 'w') as file:
#         file.write(text)

#     return send_file('domin_name.txt', as_attachment=True, attachment_filename='domin_name.txt')

# if __name__ == '__main__':
#     app.run()







###  Вариант 8

# from flask import Flask, request, send_file

# app = Flask(__name__)

# @app.route('/', methods=['GET'])
# def index():
#     return '''
#     <html>
#     <head>
#       <title>Button Example</title>
#       <script>
#         function createFile() {
#           var userInput = document.getElementById('userInput').value;
#           var xhr = new XMLHttpRequest();
#           xhr.open('POST', '/create_file', true);
#           xhr.setRequestHeader('Content-Type', 'text/plain');

#           var checks = document.getElementsByName("check");
#           var selectedChecks = [];
#           for (var i = 0; i < checks.length; i++) {
#             if (checks[i].checked) {
#               selectedChecks.push(checks[i].value);
#             }
#           }

#           var checkString = "";
#           for (var i = 0; i < selectedChecks.length; i++) {
#             if (selectedChecks[i] === "check1") {
#               checkString += "word1";
#             } else if (selectedChecks[i] === "check2") {
#               checkString += "word2";
#             }
#           }

#           var fileText = checkString + userInput;

#           xhr.send(fileText);
#         }
#       </script>
#     </head>
#     <body>
#       <input type="text" id="userInput">
#       <br>
#       <input type="checkbox" name="check" value="check1">check 1
#       <br>
#       <input type="checkbox" name="check" value="check2">check 2
#       <br>
#       <button onclick="createFile()">Create Text File</button>
#     </body>
#     </html>
#     '''

# @app.route('/create_file', methods=['POST'])
# def create_file():
#     text = request.data.decode('utf-8')
#     with open('tags_vulnerabilities.txt', 'w') as file:
#         file.write(text)

#     return send_file('tags_vulnerabilities.txt', as_attachment=True, attachment_filename='tags_vulnerabilities.txt')

# if __name__ == '__main__':
#     app.run()



# ###  Вариант 9
# from flask import Flask, request, send_file

# app = Flask(__name__)

# @app.route('/', methods=['GET'])
# def index():
#     return '''
#     <html>
#     <head>
#       <title>Button Example</title>
#       <script>
#         function createFile() {
#           var userInput = document.getElementById('userInput').value;
#           var xhr = new XMLHttpRequest();
#           xhr.open('POST', '/create_file', true);
#           xhr.setRequestHeader('Content-Type', 'text/plain');

#           var filename = "domain_name.txt";
#           var userInputData = userInput;
#           var fileData = new Blob([userInputData], {type: 'text/plain'});
#           var formData = new FormData();
#           formData.append('file', fileData, filename);
#           xhr.send(formData);

#           var checks = document.getElementsByName("check");
#           var selectedChecks = [];
#           for (var i = 0; i < checks.length; i++) {
#             if (checks[i].checked) {
#               selectedChecks.push(checks[i].value);
#             }
#           }

#           var checkString = "";
#           for (var i = 0; i < selectedChecks.length; i++) {
#             if (selectedChecks[i] === "check1") {
#               checkString += "word1";
#             } else if (selectedChecks[i] === "check2") {
#               checkString += "word2";
#             }
#           }

#           var fileText = checkString + userInput;

#           xhr.send(fileText);
#         }
#       </script>
#     </head>
#     <body>
#       <input type="text" id="userInput">
#       <br>
#       <input type="checkbox" name="check" value="check1">check 1
#       <br>
#       <input type="checkbox" name="check" value="check2">check 2
#       <br>
#       <button onclick="createFile()">Create Text File</button>
#     </body>
#     </html>
#     '''

# @app.route('/create_file', methods=['POST'])
# def create_file():
#     text = request.files.get('file').read().decode('utf-8')
#     with open('tags_vulnerabilities.txt', 'a') as file:
#         file.write(text)

#     return send_file('tags_vulnerabilities.txt', as_attachment=True, attachment_filename='tags_vulnerabilities.txt')



#  Вариант 10

# from flask import Flask, request, send_file

# app = Flask(__name__)

# @app.route('/', methods=['GET'])
# def index():
#     return '''
#     <html>
#     <head>
#       <title>Button Example</title>
#       <script>
#         function createFile() {
#           var userInput = document.getElementById('userInput').value;
#           var xhr = new XMLHttpRequest();
#           xhr.open('POST', '/create_file', true);
#           xhr.setRequestHeader('Content-Type', 'text/plain');

#           var checks = document.getElementsByName("check");
#           var selectedChecks = [];
#           for (var i = 0; i < checks.length; i++) {
#             if (checks[i].checked) {
#               selectedChecks.push(checks[i].value);
#             }
#           }

#           var checkString = "";
#           for (var i = 0; i < selectedChecks.length; i++) {
#             if (selectedChecks[i] === "check1") {
#               checkString += "word1";
#             } else if (selectedChecks[i] === "check2") {
#               checkString += "word2";
#             }
#           }

#           var fileText = checkString + userInput;

#           xhr.send(fileText);
#         }
#       </script>
#     </head>
#     <body>
#       <input type="text" id="userInput">
#       <br>
#       <input type="checkbox" name="check" value="check1">check 1
#       <br>
#       <input type="checkbox" name="check" value="check2">check 2
#       <br>
#       <button onclick="createFile()">Create Text File</button>
#     </body>
#     </html>
#     '''

# @app.route('/create_file', methods=['POST'])
# def create_file():
#     text = request.data.decode('utf-8')
#     with open('tags_vulnerabilities.txt', 'a') as file:
#         file.write(text + '\n')

#     return send_file('tags_vulnerabilities.txt', as_attachment=True, attachment_filename='tags_vulnerabilities.txt')

# @app.route('/create_domain_file', methods=['POST'])
# def create_domain_file():
#     domain_name = request.data.decode('utf-8')
#     with open('domain_name.txt', 'w') as file:
#         file.write(domain_name)

#     return send_file('domain_name.txt', as_attachment=True, attachment_filename='domain_name.txt')

# if __name__ == '__main__':
#     app.run()







# Вариант 11

# from flask import Flask, request, send_file, jsonify

# app = Flask(__name__)

# @app.route('/', methods=['GET'])
# def index():
#     # Тот же код, что и у вас для отображения HTML.
#     return '''
#     <html>
#     <head>
#       <title>Button Example</title>
#       <script>
#         function createFile() {
#           var userInput = document.getElementById('userInput').value;
#           var xhr = new XMLHttpRequest();
#           xhr.open('POST', '/create_file', true);
#           xhr.setRequestHeader('Content-Type', 'text/plain');

#           var checks = document.getElementsByName("check");
#           var selectedChecks = [];
#           for (var i = 0; i < checks.length; i++) {
#             if (checks[i].checked) {
#               selectedChecks.push(checks[i].value);
#             }
#           }

#           var checkString = "";
#           for (var i = 0; i < selectedChecks.length; i++) {
#             if (selectedChecks[i] === "check1") {
#               checkString += "word1";
#             } else if (selectedChecks[i] === "check2") {
#               checkString += "word2";
#             }
#           }

#           var fileText = checkString + userInput;

#           xhr.send(fileText);
#         }
#       </script>
#     </head>
#     <body>
#       <input type="text" id="userInput">
#       <br>
#       <input type="checkbox" name="check" value="check1">check 1
#       <br>
#       <input type="checkbox" name="check" value="check2">check 2
#       <br>
#       <button onclick="createFile()">Create Text File</button>
#     </body>
#     </html>
#     '''

# @app.route('/create_file', methods=['POST'])
# def create_file():
#     # Получаем json данные из запроса.
#     data = request.get_json()

#     # Запись слов word1 и word2 в файл tags_vulnerabilities.txt, если они есть.
#     vuln_text = data.get('vuln_text', '')
#     with open('tags_vulnerabilities.txt', 'w') as vuln_file:
#         vuln_file.write(vuln_text)

#     # Запись введённого текста пользователя в файл domain_name.txt.
#     user_text = data.get('user_text', '')
#     with open('domain_name.txt', 'w') as user_file:
#         user_file.write(user_text)

#     # Отправляем обратно информацию о сохранении файлов.
#     return jsonify({
#         'message': 'Files successfully created.',
#         'tags_vulnerabilities_file': 'tags_vulnerabilities.txt',
#         'domain_name_file': 'domain_name.txt'
#     })

# if __name__ == '__main__':
#     app.run()




















###  Вариант 4

# from flask import Flask, request, send_file

# app = Flask(__name__)

# @app.route('/', methods=['GET'])
# def index():
#     return '''
#     <html>
#     <head>
#       <title>Button Example</title>
#       <script>
#         function createFile() {
#           var xhr = new XMLHttpRequest();
#           xhr.open('POST', '/create_file', true);
#           xhr.send();
#         }
#       </script>
#     </head>
#     <body>
#       <button onclick="createFile()">Create Text File</button>
#     </body>
#     </html>
#     '''

# @app.route('/create_file', methods=['POST'])
# def create_file():
#     with open('comand.txt', 'w') as file:
#         file.write('33333')

#     return send_file('comand.txt', as_attachment=True, attachment_filename='comand.txt')

# if __name__ == '__main__':
#     app.run()





#  Вариант  6

# from flask import Flask, request, send_file

# app = Flask(__name__)

# @app.route('/', methods=['GET'])
# def index():
#     return '''
#     <html>
#     <head>
#     <title>Button Example</title>
#     </head>
#     <body>
#     <input type="text" id="textInput">
#     <input type="checkbox" id="checkbox1">Checkbox 1
#     <input type="checkbox" id="checkbox2">Checkbox 2
#     <input type="checkbox" id="checkbox3">Checkbox 3
#     <button onclick="start()">Start</button>
#     <script src="script.js"></script>
#     </body>
#     </html>
#     '''

# @app.route('/start', methods=['POST'])
# def start():
#     text_input = request.form.get('text')
#     checkbox1 = request.form.get('checkbox1')
#     checkbox2 = request.form.get('checkbox2')
#     checkbox3 = request.form.get('checkbox3')
    
#     if checkbox1:
#         tags_vulnerabilities = 'vulnerability1'
#     else:
#         tags_vulnerabilities = ''
    
#     if checkbox2:
#         tags_vulnerabilities += 'vulnerability2'
    
#     if checkbox3:
#         tags_vulnerabilities += 'vulnerability3'
    
#     with open('domain_name.txt', 'w') as file:
#         file.write(text_input)
    
#     with open('tags_vulnerabilities.txt', 'w') as file:
#         file.write(tags_vulnerabilities)

#     return send_file('domain_name.txt', as_attachment=True, attachment_filename='domain_name.txt')

# if __name__ == '__main__':
#     app.run()






###  Вариант 1

# import sys

# def main():
#     command_args = " ".join(sys.argv[1:])
#     # Далее выполняется действие в зависимости от переданной команды
#     print("Команда выполнена:", command_args)

# if __name__ == "__main__":
#     main()






###  Вариант 12


###  Вариант 4

# from flask import Flask, request, send_file
# import json

# app = Flask(__name__)

# @app.route('/', methods=['GET'])
# def index():
#     return '''
#     <html>
#     <head>
#       <title>Button Example</title>
#       <script>
#         function createFile() {
#           var text = document.getElementById('inputField').value;  // Den eingegebenen Text aus dem Texteingabefeld abrufen
#           var file = new File([text], 'comand.txt', {type: 'text/plain'});
#           var url = URL.createObjectURL(file);
#           var a = document.createElement('a');
#           a.href = url;
#           a.download = 'comand.txt';
#           a.style.display = 'none';
#           document.body.appendChild(a);
#           a.click();
#           document.body.removeChild(a);
#           URL.revokeObjectURL(url);
#         }
#       </script>
#     </head>
#     <body>
#       <input type="text" id="inputField" placeholder="Enter text here">
#       <button onclick="createFile()">Create Text File</button>
#     </body>
#     </html>
#     '''


# @app.route('/create_file', methods=['POST'])
# def create_file():
#     text = request.form.get('input_text')  # Den eingegebenen Text aus dem Formular abrufen
#     with open('comand.txt', 'w') as file:
#         file.write(text)  # Den eingegebenen Text in die Datei schreiben
#     return send_file('comand.txt', as_attachment=True, attachment_filename='comand.txt')


# if __name__ == '__main__':
#     app.run()






###  Вариант 7

# from flask import Flask, request, send_file

# app = Flask(__name__)

# @app.route('/', methods=['GET'])
# def index():
#     return '''
#     <html>
#     <head>
#       <title>Button Example</title>
#       <script>
#         function createFile() {
#           var userInput = document.getElementById('userInput').value;
#           var xhr = new XMLHttpRequest();
#           xhr.open('POST', '/create_file', true);
#           xhr.setRequestHeader('Content-Type', 'text/plain');
#           xhr.send(userInput);
#         }
#       </script>
#     </head>
#     <body>
#       <input type="text" id="userInput">
#       <button onclick="createFile()">Create Text File</button>
#     </body>
#     </html>
#     '''

# @app.route('/create_file', methods=['POST'])
# def create_file():
#     text = request.data.decode('utf-8')
#     with open('domin_name.txt', 'w') as file:
#         file.write(text)

#     return send_file('domin_name.txt', as_attachment=True, attachment_filename='domin_name.txt')

# if __name__ == '__main__':
#     app.run()






###  Вариант 13

# from flask import Flask, request, send_file

# app = Flask(__name__)

# @app.route('/', methods=['GET'])
# def index():
#     return '''
#     <html>
#     <head>
#       <title>Button Example</title>
#       <script>
#         function createFile() {
#           var userInput = document.getElementById('userInput').value;
#           var xhr = new XMLHttpRequest();
#           xhr.open('POST', '/create_file', true);
#           xhr.setRequestHeader('Content-Type', 'text/plain');
#           xhr.send(userInput);
#         }
#       </script>
#     </head>
#     <body>
#       <input type="text" id="userInput">
#       <button onclick="createFile()">Create Text File</button>
#     </body>
#     </html>
#     '''

# @app.route('/create_file', methods=['POST'])
# def create_file():
#     text = request.data.decode('utf-8')
#     with open('domin_name.txt', 'w') as file:
#         file.write(text)

#     return send_file('domin_name.txt', as_attachment=True, attachment_filename='domin_name.txt')

# if __name__ == '__main__':
#     app.run()





###  Вариант 14

# from flask import Flask, request, send_file

# app = Flask(__name__)

# @app.route('/', methods=['GET'])
# def index():
#     return '''
#     <html>
#     <head>
#       <title>Button Example</title>
#       <script>
#         function createFile() {
#           var userInput = document.getElementById('userInput').value;
#           var xhr = new XMLHttpRequest();
#           xhr.open('POST', '/create_file', true);
#           xhr.setRequestHeader('Content-Type', 'text/plain');

#           var checks = document.getElementsByName("check");
#           var selectedChecks = [];
#           for (var i = 0; i < checks.length; i++) {
#             if (checks[i].checked) {
#               selectedChecks.push(checks[i].value);
#             }
#           }

#           var checkString = "";
#           for (var i = 0; i < selectedChecks.length; i++) {
#             if (selectedChecks[i] === "check1") {
#               checkString += "Point_1";
#             } else if (selectedChecks[i] === "check2") {
#               checkString += "Point_2";
#             }
#           }

#           var fileText = checkString + userInput;

#           xhr.send(fileText);
#         }
#       </script>
#     </head>
#     <body>
#       <input type="text" id="userInput">
#       <br>
#       <input type="checkbox" name="check" value="check1">check 1
#       <br>
#       <input type="checkbox" name="check" value="check2">check 2
#       <br>
#       <button onclick="createFile()">Create Text File</button>
#     </body>
#     </html>
#     '''

# @app.route('/create_file', methods=['POST'])
# def create_file():
#     text = request.data.decode('utf-8')
#     with open('domin_name.txt', 'w') as file:
#         file.write(text)

#     with open('tags_vulnerabilities.txt', 'w') as file:
#         file.write(text)

#     return send_file('domin_name.txt', as_attachment=True, attachment_filename='domin_name.txt')

# if __name__ == '__main__':
#     app.run()






###  Вариант 15

# from flask import Flask, request, send_file
# import os

# app = Flask(__name__)

# @app.route('/', methods=['GET'])
# def index():
#     return '''
#     <html>
#     <head>
#       <title>Button Example</title>
#       <script>
#         function createFile() {
#           var userInput = document.getElementById('domen_name').value;
#           var chek1 = document.getElementById('chek_1').checked;
#           var chek2 = document.getElementById('chek_2').checked;
          
#           var xhr = new XMLHttpRequest();
#           xhr.open('POST', '/create_file', true);
#           xhr.setRequestHeader('Content-Type', 'text/plain');
#           var requestBody = userInput + ',' + (chek1 ? 'Point_1,' : '') + (chek2 ? 'Point_2' : '');
#           xhr.send(requestBody);
#         }
#       </script>
#     </head>
#     <body>
#       <input type="text" id="domen_name">
#       <input type="checkbox" id="chek_1"> Point_1
#       <input type="checkbox" id="chek_2"> Point_2
#       <button onclick="createFile()">Create Text File</button>
#     </body>
#     </html>
#     '''

# @app.route('/create_file', methods=['POST'])
# def create_file():
#     text = request.data.decode('utf-8').split(',')[0]
#     with open('domin_name.txt', 'w') as file:
#         file.write(text)

#     tags_vulnerabilities = request.data.decode('utf-8').split(',')[1:]
#     with open('tags_vulnerabilities.txt', 'w') as file:
#         file.write(','.join(tags_vulnerabilities))

#     return send_file('domin_name.txt', as_attachment=True, attachment_filename='domin_name.txt')

# if __name__ == '__main__':
#     app.run()





###  Вариант 16

# from flask import Flask, request, send_file
# import os

# app = Flask(__name__)

# @app.route('/', methods=['GET'])
# def index():
#     return '''
#     <html>
#     <head>
#       <title>Button Example</title>
#       <script>
#         function createFile() {
#           var userInput = document.getElementById('domen_name').value;
#           var chek1 = document.getElementById('chek_1').checked;
#           var chek2 = document.getElementById('chek_2').checked;
          
#           var xhr = new XMLHttpRequest();
#           xhr.open('POST', '/create_file', true);
#           xhr.setRequestHeader('Content-Type', 'text/plain');
#           var requestBody = userInput + ',' + (chek1 ? 'Point_1,' : '') + (chek2 ? 'Point_2' : '');
#           xhr.send(requestBody);
#         }
#       </script>
#     </head>
#     <body>
#       <input type="text" id="domen_name">
#       <input type="checkbox" id="chek_1"> Point_1
#       <input type="checkbox" id="chek_2"> Point_2
#       <button onclick="createFile()">Create Text File</button>
#     </body>
#     </html>
#     '''

# @app.route('/create_file', methods=['POST'])
# def create_file():
#     text = request.data.decode('utf-8').split(',')[0]
#     with open('domin_name.txt', 'w') as file:
#         file.write(text)

#     tags_vulnerabilities = request.data.decode('utf-8').split(',')[1:]
#     with open('tags_vulnerabilities.txt', 'w') as file:
#         file.write(','.join(tags_vulnerabilities))

#     with open('tags_vulnerabilities.txt', 'r') as file:
#         data = file.read()
#     if data.startswith(','):
#         data = data[1:]
#     if data.endswith(','):
#         data = data[:-1]
#     with open('tags_vulnerabilities.txt', 'w') as file:
#         file.write(data)

#     return send_file('domin_name.txt', as_attachment=True, attachment_filename='domin_name.txt')

# if __name__ == '__main__':
#     app.run()





###  Вариант 17

# from flask import Flask, request, send_file
# import os

# app = Flask(__name__)

# @app.route('/', methods=['GET'])
# def index():
#     return '''
#     <html>
#     <head>
#       <title>Button Example</title>
#       <script>
#         function createFile() {
#           var userInput = document.getElementById('domen_name').value;
#           var cve = document.getElementById('cve').checked;
#           var panel = document.getElementById('panel').checked;
#           var wordpress = document.getElementById('wordpress').checked;
#           var xss = document.getElementById('xss').checked;
#           var exposure = document.getElementById('exposure').checked;
#           var wpPlugin = document.getElementById('wp-plugin').checked;
#           var osint = document.getElementById('osint').checked;
#           var tech = document.getElementById('tech').checked;
#           var lfi = document.getElementById('lfi').checked;
#           var edb = document.getElementById('edb').checked;
          
#           var xhr = new XMLHttpRequest();
#           xhr.open('POST', '/create_file', true);
#           xhr.setRequestHeader('Content-Type', 'text/plain');
#           var requestBody = userInput + ',' + (cve ? 'CVE,' : '') + (panel ? 'Panel,' : '') + (wordpress ? 'Wordpress,' : '') + (xss ? 'XSS,' : '') + 
#                             (exposure ? 'Exposure,' : '') + (wpPlugin ? 'WP-Plugin,' : '') + (osint ? 'OSINT,' : '') + (tech ? 'Tech,' : '') + 
#                             (lfi ? 'LFI,' : '') + (edb ? 'EDB' : '');
#           xhr.send(requestBody);
#         }
#       </script>
#     </head>
#     <body>
#       <input type="text" id="domen_name">
#       <input type="checkbox" id="cve"> CVE
#       <input type="checkbox" id="panel"> Panel
#       <input type="checkbox" id="wordpress"> Wordpress
#       <input type="checkbox" id="xss"> XSS
#       <input type="checkbox" id="exposure"> Exposure
#       <input type="checkbox" id="wp-plugin"> WP-Plugin
#       <input type="checkbox" id="osint"> OSINT
#       <input type="checkbox" id="tech"> Tech
#       <input type="checkbox" id="lfi"> LFI
#       <input type="checkbox" id="edb"> EDB
#       <button onclick="createFile()">Create Text File</button>
#     </body>
#     </html>
#     '''

# @app.route('/create_file', methods=['POST'])
# def create_file():
#     text = request.data.decode('utf-8').split(',')[0]
#     with open('domin_name.txt', 'w') as file:
#         file.write(text)

#     tags_vulnerabilities = request.data.decode('utf-8').split(',')[1:]
#     with open('tags_vulnerabilities.txt', 'w') as file:
#         file.write(','.join(tags_vulnerabilities))

#     with open('tags_vulnerabilities.txt', 'r') as file:
#         data = file.read()
#     if data.startswith(','):
#         data = data[1:]
#     if data.endswith(','):
#         data = data[:-1]
#     with open('tags_vulnerabilities.txt', 'w') as file:
#         file.write(data)

#     return send_file('domin_name.txt', as_attachment=True, attachment_filename='domin_name.txt')

# if __name__ == '__main__':
#     app.run()






###  Вариант 18

# from flask import Flask, request, send_file
# import os

# app = Flask(__name__)

# @app.route('/', methods=['GET'])
# def index():
#     return '''
#     <html>
#     <head>
#       <title>Button Example</title>
#       <script>
#         function createFile() {
#             var userInput = document.getElementById('domen_name').value;
#             var text = userInput || '33333';
#             var file = new File([text], 'domin_name.txt', {type: 'text/plain'});
#             var url = URL.createObjectURL(file);

#             var a = document.createElement('a');
#             a.href = url;
#             a.download = 'domin_name.txt';
#             a.style.display = 'none';
#             document.body.appendChild(a);

#             a.click();

#             document.body.removeChild(a);
#             URL.revokeObjectURL(url);

#             var cve = document.getElementById('cve').checked ? 'CVE,' : '';
#             var panel = document.getElementById('panel').checked ? 'Panel,' : '';
#             var wordpress = document.getElementById('wordpress').checked ? 'Wordpress,' : '';
#             var xss = document.getElementById('xss').checked ? 'XSS,' : '';
#             var exposure = document.getElementById('exposure').checked ? 'Exposure,' : '';
#             var wpPlugin = document.getElementById('wp-plugin').checked ? 'WP-Plugin,' : '';
#             var osint = document.getElementById('osint').checked ? 'OSINT,' : '';
#             var tech = document.getElementById('tech').checked ? 'Tech,' : '';
#             var lfi = document.getElementById('lfi').checked ? 'LFI,' : '';
#             var edb = document.getElementById('edb').checked ? 'EDB,' : '';
#             var info = document.getElementById('info').checked ? 'info,' : '';
#             var high = document.getElementById('high').checked ? 'high,' : '';
#             var medium = document.getElementById('medium').checked ? 'medium,' : '';
#             var critical = document.getElementById('critical').checked ? 'critical,' : '';
#             var low = document.getElementById('low').checked ? 'low,' : '';
#             var unknown = document.getElementById('unknown').checked ? 'unknown' : '';
#             var tags_vulnerabilities = cve + panel + wordpress + xss + exposure + wpPlugin + osint + tech + lfi + edb + info + high + medium + critical + low + unknown;

#             var xhr = new XMLHttpRequest();
#             xhr.open('POST', '/create_file', true);
#             xhr.setRequestHeader('Content-Type', 'text/plain');
#             xhr.send(text + ',' + tags_vulnerabilities);
#         }
#       </script>
#     </head>
#     <body>
#         <input type="text" id="domen_name">
#         <input type="checkbox" id="cve"> CVE
#         <input type="checkbox" id="panel"> Panel
#         <input type="checkbox" id="wordpress"> Wordpress
#         <input type="checkbox" id="xss"> XSS
#         <input type="checkbox" id="exposure"> Exposure
#         <input type="checkbox" id="wp-plugin"> WP-Plugin
#         <input type="checkbox" id="osint"> OSINT
#         <input type="checkbox" id="tech"> Tech
#         <input type="checkbox" id="lfi"> LFI
#         <input type="checkbox" id="edb"> EDB
#         <input type="checkbox" id="info"> Info
#         <input type="checkbox" id="high"> High
#         <input type="checkbox" id="medium"> Medium
#         <input type="checkbox" id="critical"> Critical
#         <input type="checkbox" id="low"> Low
#         <input type="checkbox" id="unknown"> Unknown
#         <button onclick="createFile()">Create Text File</button>
#     </body>
#     '''

# @app.route('/create_file', methods=['POST'])
# def create_file():
#     text = request.data.decode('utf-8').split(',')[0]
#     with open('domin_name.txt', 'w') as file:
#         file.write(text)

#     tags_vulnerabilities = request.data.decode('utf-8').split(',')[1:]
#     with open('tags_vulnerabilities.txt', 'w') as file:
#         file.write(','.join(tags_vulnerabilities))

#     tags_vulnerabilities = request.data.decode('utf-8').split(',')[1:]
#     with open('severity_vulnerabilities.txt', 'w') as file:
#         file.write(','.join(tags_vulnerabilities))

#     with open('tags_vulnerabilities.txt', 'r') as file:
#         data = file.read()
#     if data.startswith(','):
#         data = data[1:]
#     if data.endswith(','):
#         data = data[:-1]
#     with open('tags_vulnerabilities.txt', 'w') as file:
#         file.write(data)

#     return send_file('domin_name.txt', as_attachment=True, attachment_filename='domin_name.txt')

# if __name__ == '__main__':
#     app.run()






###  Вариант 20

# from flask import Flask, request, send_file
# import os

# app = Flask(__name__)

# @app.route('/', methods=['GET'])
# def index():
#     return '''
#     <html>
#     <head>
#     <title>Button Example</title>
#     <script>
#         function createFile() {
#             var userInput = document.getElementById('domen_name').value;
#             var text = userInput || '33333';
#             var file = new File([text], 'domin_name.txt', {type: 'text/plain'});
#             var url = URL.createObjectURL(file);

#             var a = document.createElement('a');
#             a.href = url;
#             a.download = 'domin_name.txt';
#             a.style.display = 'none';
#             document.body.appendChild(a);

#             a.click();

#             document.body.removeChild(a);
#             URL.revokeObjectURL(url);

#             // Получение значений для всех чекбоксов
#             var cve = document.getElementById('cve').checked ? 'CVE,' : '';
#             var panel = document.getElementById('panel').checked ? 'Panel,' : '';
#             var wordpress = document.getElementById('wordpress').checked ? 'Wordpress,' : '';
#             var xss = document.getElementById('xss').checked ? 'XSS,' : '';
#             var exposure = document.getElementById('exposure').checked ? 'Exposure,' : '';
#             var wpPlugin = document.getElementById('wp-plugin').checked ? 'WP-Plugin,' : '';
#             var osint = document.getElementById('osint').checked ? 'OSINT,' : '';
#             var tech = document.getElementById('tech').checked ? 'Tech,' : '';
#             var lfi = document.getElementById('lfi').checked ? 'LFI,' : '';
#             var edb = document.getElementById('edb').checked ? 'EDB,' : '';
#             // Добавление новых чекбоксов
#             var info = document.getElementById('info').checked ? 'Info,' : '';
#             var high = document.getElementById('high').checked ? 'High' : ''; // Без запятой, т.к. последний элемент
#             var tags_vulnerabilities = cve + panel + wordpress + xss + exposure + wpPlugin + osint + tech + lfi + edb + info + high;

#             var xhr = new XMLHttpRequest();
#             xhr.open('POST', '/create_file', true);
#             xhr.setRequestHeader('Content-Type', 'text/plain');
#             xhr.send(text + ',' + tags_vulnerabilities);
#         }
#     </script>
#     </head>
#     <body>
#         <input type="text" id="domen_name">
#         <input type="checkbox" id="cve"> CVE
#         <input type="checkbox" id="panel"> Panel
#         <input type="checkbox" id="wordpress"> Wordpress
#         <input type="checkbox" id="xss"> XSS
#         <input type="checkbox" id="exposure"> Exposure
#         <input type="checkbox" id="wp-plugin"> WP-Plugin
#         <input type="checkbox" id="osint"> OSINT
#         <input type="checkbox" id="tech"> Tech
#         <input type="checkbox" id="lfi"> LFI
#         <input type="checkbox" id="edb"> EDB
#         <input type="checkbox" id="info"> Info
#         <input type="checkbox" id="high"> High
#         <button onclick="createFile()">Create Text File</button>
#     </body>
#     </html>
#     '''

# @app.route('/create_file', methods=['POST'])
# def create_file():
#     text = request.data.decode('utf-8').split(',')[0]
#     with open('domin_name.txt', 'w') as file:
#         file.write(text)

#     tags_vulnerabilities = request.data.decode('utf-8').split(',')[1:-2] # Изменено срезание до -2, чтобы исключить info и high
#     with open('tags_vulnerabilities.txt', 'w') as file:
#         file.write(','.join(tags_vulnerabilities))

#     severity = request.data.decode('utf-8').split(',')[-2:]  # Получаем последние два элемента
#     with open('severity_vulnerabilities.txt', 'w') as file:  # Пишем в новый файл
#         file.write(','.join(severity))

#     return send_file('domin_name.txt', as_attachment=True, attachment_filename='domin_name.txt')

# if __name__ == '__main__':
#     app.run()








###  Вариант 21

# from flask import Flask, request, send_file
# import os

# app = Flask(__name__)

# @app.route('/', methods=['GET'])
# def index():
#     return '''
#     <html>
#     <head>
#     <title>Button Example</title>
#     <script>
#         function sendDomainName() {
#             var userInput = document.getElementById('domain_name').value;
#             var xhr = new XMLHttpRequest();
#             xhr.open('POST', '/create_domain_file', true);
#             xhr.setRequestHeader('Content-Type', 'text/plain');
#             xhr.send(userInput);
#         }

#         function sendVulnerabilityTags() {
#             var cve = document.getElementById('cve').checked ? 'CVE,' : '';
#             var panel = document.getElementById('panel').checked ? 'Panel,' : '';
#             var wordpress = document.getElementById('wordpress').checked ? 'Wordpress,' : '';
#             var xss = document.getElementById('xss').checked ? 'XSS,' : '';
#             var exposure = document.getElementById('exposure').checked ? 'Exposure,' : '';
#             var wpPlugin = document.getElementById('wp-plugin').checked ? 'WP-Plugin,' : '';
#             var osint = document.getElementById('osint').checked ? 'OSINT,' : '';
#             var tech = document.getElementById('tech').checked ? 'Tech,' : '';
#             var lfi = document.getElementById('lfi').checked ? 'LFI,' : '';
#             var edb = document.getElementById('edb').checked ? 'EDB,' : '';
#             var tags_vulnerabilities = cve + panel + wordpress + xss + exposure + wpPlugin + osint + tech + lfi + edb;

#             var xhr = new XMLHttpRequest();
#             xhr.open('POST', '/create_tags_file', true);
#             xhr.setRequestHeader('Content-Type', 'text/plain');
#             xhr.send(tags_vulnerabilities.slice(0, -1)); // Удаляем последнюю запятую
#         }

#         function sendSeverity() {
#             var info = document.getElementById('info').checked ? 'Info,' : '';
#             var high = document.getElementById('high').checked ? 'High,' : '';
#             var severity = info + high;

#             var xhr = new XMLHttpRequest();
#             xhr.open('POST', '/create_severity_file', true);
#             xhr.setRequestHeader('Content-Type', 'text/plain');
#             xhr.send(severity.slice(0, -1));
#         }
#     </script>
#     </head>
#     <body>
#         <input type="text" id="domain_name">
#         <input type="checkbox" id="cve"> CVE
#         <input type="checkbox" id="panel"> Panel
#         <input type="checkbox" id="wordpress"> Wordpress
#         <input type="checkbox" id="xss"> XSS
#         <input type="checkbox" id="exposure"> Exposure
#         <input type="checkbox" id="wp-plugin"> WP-Plugin
#         <input type="checkbox" id="osint"> OSINT
#         <input type="checkbox" id="tech"> Tech
#         <input type="checkbox" id="lfi"> LFI
#         <input type="checkbox" id="edb"> EDB
#         <input type="checkbox" id="info"> Info
#         <input type="checkbox" id="high"> High
#         <button onclick="sendDomainName()">Send Domain Name</button>
#         <button onclick="sendVulnerabilityTags()">Send Vulnerability Tags</button>
#         <button onclick="sendSeverity()">Send Severity</button>
#     </body>
#     </html>
#     '''


# @app.route('/create_domain_file', methods=['POST'])
# def create_domain_file():
#     text = request.data.decode('utf-8')
#     with open('domain_name.txt', 'w') as file:
#         file.write(text)
#     return 'Domain name saved'

# @app.route('/create_tags_file', methods=['POST'])
# def create_tags_file():
#     tags = request.data.decode('utf-8')
#     with open('tags_vulnerabilities.txt', 'w') as file:
#         file.write(tags)
#     return 'Tags saved'

# @app.route('/create_severity_file', methods=['POST'])
# def create_severity_file():
#     severity = request.data.decode('utf-8')
#     with open('severity_vulnerabilities.txt', 'w') as file:
#         file.write(severity)
#     return 'Severity saved'

# if __name__ == '__main__':
#     app.run()










###  Вариант 21

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
        os.system('cd automated_scanning && docker-compose run docker_scan')
        return 'Scan command executed'
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run()