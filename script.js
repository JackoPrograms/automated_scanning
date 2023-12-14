//  Вариант 6

// function start() {
//     var textInput = document.getElementById('textInput').value;
//     var checkbox1 = document.getElementById('checkbox1').checked;
//     var checkbox2 = document.getElementById('checkbox2').checked;
//     var checkbox3 = document.getElementById('checkbox3').checked;
    
//     var xhr = new XMLHttpRequest();
//     xhr.open("POST", "/start", true);
//     xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
//     xhr.send("text=" + textInput + "&checkbox1=" + checkbox1 + "&checkbox2=" + checkbox2 + "&checkbox3=" + checkbox3);
// }







// function saveFile() {
//     var xhr = new XMLHttpRequest();
//     xhr.open("POST", '/create_files', true);
//     xhr.send();
// }
  





// function saveFile() {
//     var text = document.getElementById("text").value;
//     var checkboxes = Array.from(document.querySelectorAll('input[type="checkbox"]:checked')).map(c => c.id);
    
//     var xhr = new XMLHttpRequest();
//     xhr.open("POST", "create_file", true);
//     xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    
//     var data = "text=" + encodeURIComponent(text);
//     for (var i = 0; i < checkboxes.length; i++) {
//         data += "&checkbox=" + encodeURIComponent(checkboxes[i]);
//     }
    
//     xhr.send(data);
// }






// function start() {
//     var textInput = document.getElementById('text_input').value;
//     var checkbox1 = document.getElementById('checkbox1').checked;
//     var checkbox2 = document.getElementById('checkbox2').checked;
//     var checkbox3 = document.getElementById('checkbox3').checked;
    
//     var xhr = new XMLHttpRequest();
//     xhr.open("POST", "create_files", true);
//     xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
//     xhr.send("text_input=" + textInput + "&checkbox1=" + checkbox1 + "&checkbox2=" + checkbox2 + "&checkbox3=" + checkbox3);
// }






// function saveFiles() {
//     var xhr = new XMLHttpRequest();
//     xhr.open("POST", '/create_file', true);
//     xhr.send(new FormData(document.getElementById("form")));
// }





// function saveFile() {
//     var xhr = new XMLHttpRequest();
//     xhr.open("POST", "save_file.py", true);
//     xhr.send();
// }














//  Вариант 6

// function start() {
//     var textInput = document.getElementById('textInput').value;
//     var checkbox1 = document.getElementById('checkbox1').checked;
//     var checkbox2 = document.getElementById('checkbox2').checked;
//     var checkbox3 = document.getElementById('checkbox3').checked;
    
//     var xhr = new XMLHttpRequest();
//     xhr.open("POST", "/start", true);
//     xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
//     xhr.send("text=" + textInput + "&checkbox1=" + checkbox1 + "&checkbox2=" + checkbox2 + "&checkbox3=" + checkbox3);
// }





//  Вариант 1

// function generateCommand() {
//     var command = "";
//     var checkboxes = document.querySelectorAll('input[type="checkbox"]:checked');
//     checkboxes.forEach(function(checkbox) {
//         command += checkbox.name + " ";
//     });

//     if (command !== "") {
//         command = "python script.py " + command.trim();
//         sendCommand(command);
//     }
// }

// function sendCommand(command) {
//     // Передача команды на сервер или выполнение локально
//     // В данном примере будет выполнено локально на компьютере, где запущен браузер

//     var xhr = new XMLHttpRequest();
//     xhr.open("GET", "http://localhost:5000/?command=" + encodeURIComponent(command), true);
//     xhr.onreadystatechange = function() {
//         if (xhr.readyState === 4 && xhr.status === 200) {
//             console.log(xhr.responseText);
//         }
//     };
//     xhr.send();
// }






//  Вариант 12

// function createFile() {
//     var text = document.getElementById('inputField').value;  // Den eingegebenen Text aus dem Texteingabefeld abrufen
//     var file = new File([text], 'comand.txt', {type: 'text/plain'});
//     var url = URL.createObjectURL(file);
//     var a = document.createElement('a');
//     a.href = url;
//     a.download = 'comand.txt';
//     a.style.display = 'none';
//     document.body.appendChild(a);
//     a.click();
//     document.body.removeChild(a);
//     URL.revokeObjectURL(url);
// }





//  Вариант 13

// function createFile() {
//     var userInput = document.getElementById('userInput').value;
//     var text = userInput || '33333';
//     var file = new File([text], 'domin_name.txt', {type: 'text/plain'});
//     var url = URL.createObjectURL(file);

//     var a = document.createElement('a');
//     a.href = url;
//     a.download = 'domin_name.txt';
//     a.style.display = 'none';
//     document.body.appendChild(a);

//     a.click();

//     document.body.removeChild(a);
//     URL.revokeObjectURL(url);
// }






//  Вариант 14

// function createFile() {
//     var userInput = document.getElementById('userInput').value;
//     var text = userInput || '33333';

//     var checks = document.getElementsByName("check");
//     var selectedChecks = [];
//     for (var i = 0; i < checks.length; i++) {
//         if (checks[i].checked) {
//             selectedChecks.push(checks[i].value);
//         }
//     }

//     var checkString = "";
//     for (var i = 0; i < selectedChecks.length; i++) {
//         if (selectedChecks[i] === "check1") {
//             checkString += "Point_1";
//         } else if (selectedChecks[i] === "check2") {
//             checkString += "Point_2";
//         }
//     }

//     var fileText = checkString + text;

//     var file = new File([fileText], 'domin_name.txt', {type: 'text/plain'});
//     var url = URL.createObjectURL(file);

//     var a = document.createElement('a');
//     a.href = url;
//     a.download = 'domin_name.txt';
//     a.style.display = 'none';
//     document.body.appendChild(a);

//     a.click();

//     document.body.removeChild(a);
//     URL.revokeObjectURL(url);
// }






//  Вариант 15

// function createFile() {
//     var userInput = document.getElementById('domen_name').value;
//     var text = userInput || '33333';
//     var file = new File([text], 'domin_name.txt', {type: 'text/plain'});
//     var url = URL.createObjectURL(file);

//     var a = document.createElement('a');
//     a.href = url;
//     a.download = 'domin_name.txt';
//     a.style.display = 'none';
//     document.body.appendChild(a);

//     a.click();

//     document.body.removeChild(a);
//     URL.revokeObjectURL(url);

//     var chek1 = document.getElementById('chek_1').checked ? 'Point_1,' : '';
//     var chek2 = document.getElementById('chek_2').checked ? 'Point_2' : '';
//     var tags_vulnerabilities = chek1 + chek2;

//     var xhr = new XMLHttpRequest();
//     xhr.open('POST', '/create_file', true);
//     xhr.setRequestHeader('Content-Type', 'text/plain');
//     xhr.send(text + ',' + tags_vulnerabilities);
// }




//  Вариант 16

// function createFile() {
//     var userInput = document.getElementById('domen_name').value;
//     var text = userInput || '33333';
//     var file = new File([text], 'domin_name.txt', {type: 'text/plain'});
//     var url = URL.createObjectURL(file);

//     var a = document.createElement('a');
//     a.href = url;
//     a.download = 'domin_name.txt';
//     a.style.display = 'none';
//     document.body.appendChild(a);

//     a.click();

//     document.body.removeChild(a);
//     URL.revokeObjectURL(url);

//     var chek1 = document.getElementById('chek_1').checked ? 'Point_1,' : '';
//     var chek2 = document.getElementById('chek_2').checked ? 'Point_2' : '';
//     var tags_vulnerabilities = chek1 + chek2;

//     var xhr = new XMLHttpRequest();
//     xhr.open('POST', '/create_file', true);
//     xhr.setRequestHeader('Content-Type', 'text/plain');
//     xhr.send(text + ',' + tags_vulnerabilities);
// }






//  Вариант 17

// function createFile() {
//     var userInput = document.getElementById('domen_name').value;
//     var text = userInput || '33333';
//     var file = new File([text], 'domin_name.txt', {type: 'text/plain'});
//     var url = URL.createObjectURL(file);

//     var a = document.createElement('a');
//     a.href = url;
//     a.download = 'domin_name.txt';
//     a.style.display = 'none';
//     document.body.appendChild(a);

//     a.click();

//     document.body.removeChild(a);
//     URL.revokeObjectURL(url);

//     var cve = document.getElementById('cve').checked ? 'cve,' : '';
//     var panel = document.getElementById('panel').checked ? 'Panel' : '';
//     var tags_vulnerabilities = cve + panel;

//     var xhr = new XMLHttpRequest();
//     xhr.open('POST', '/create_file', true);
//     xhr.setRequestHeader('Content-Type', 'text/plain');
//     xhr.send(text + ',' + tags_vulnerabilities);
// }




//  Вариант 18

// function createFile() {
//     var userInput = document.getElementById('domen_name').value;
//     var text = userInput || '33333';
//     var file = new File([text], 'domin_name.txt', {type: 'text/plain'});
//     var url = URL.createObjectURL(file);

//     var a = document.createElement('a');
//     a.href = url;
//     a.download = 'domin_name.txt';
//     a.style.display = 'none';
//     document.body.appendChild(a);

//     a.click();

//     document.body.removeChild(a);
//     URL.revokeObjectURL(url);

//     var cve = document.getElementById('cve').checked ? 'CVE,' : '';
//     var panel = document.getElementById('panel').checked ? 'Panel,' : '';
//     var wordpress = document.getElementById('wordpress').checked ? 'Wordpress,' : '';
//     var xss = document.getElementById('xss').checked ? 'XSS,' : '';
//     var exposure = document.getElementById('exposure').checked ? 'Exposure,' : '';
//     var wpPlugin = document.getElementById('wp-plugin').checked ? 'WP-Plugin,' : '';
//     var osint = document.getElementById('osint').checked ? 'OSINT,' : '';
//     var tech = document.getElementById('tech').checked ? 'Tech,' : '';
//     var lfi = document.getElementById('lfi').checked ? 'LFI,' : '';
//     var edb = document.getElementById('edb').checked ? 'EDB' : '';
//     var tags_vulnerabilities = cve + panel + wordpress + xss + exposure + wpPlugin + osint + tech + lfi + edb;

//     var xhr = new XMLHttpRequest();
//     xhr.open('POST', '/create_file', true);
//     xhr.setRequestHeader('Content-Type', 'text/plain');
//     xhr.send(text + ',' + tags_vulnerabilities);
// }





//  Вариант 19

// function createFile() {
//     var userInput = document.getElementById('domen_name').value;
//     var text = userInput || '33333';
//     var file = new File([text], 'domin_name.txt', {type: 'text/plain'});
//     var url = URL.createObjectURL(file);

//     var a = document.createElement('a');
//     a.href = url;
//     a.download = 'domin_name.txt';
//     a.style.display = 'none';
//     document.body.appendChild(a);

//     a.click();

//     document.body.removeChild(a);
//     URL.revokeObjectURL(url);

//     var cve = document.getElementById('cve').checked ? 'CVE,' : '';
//     var panel = document.getElementById('panel').checked ? 'Panel,' : '';
//     var wordpress = document.getElementById('wordpress').checked ? 'Wordpress,' : '';
//     var xss = document.getElementById('xss').checked ? 'XSS,' : '';
//     var exposure = document.getElementById('exposure').checked ? 'Exposure,' : '';
//     var wpPlugin = document.getElementById('wp-plugin').checked ? 'WP-Plugin,' : '';
//     var osint = document.getElementById('osint').checked ? 'OSINT,' : '';
//     var tech = document.getElementById('tech').checked ? 'Tech,' : '';
//     var lfi = document.getElementById('lfi').checked ? 'LFI,' : '';
//     var edb = document.getElementById('edb').checked ? 'EDB,' : '';
//     var info = document.getElementById('info').checked ? 'info,' : '';
//     var high = document.getElementById('high').checked ? 'high,' : '';
//     var medium = document.getElementById('medium').checked ? 'medium,' : '';
//     var critical = document.getElementById('critical').checked ? 'critical,' : '';
//     var low = document.getElementById('low').checked ? 'low,' : '';
//     var unknown = document.getElementById('unknown').checked ? 'unknown' : '';
//     var tags_vulnerabilities = cve + panel + wordpress + xss + exposure + wpPlugin + osint + tech + lfi + edb + info + high + medium + critical + low + unknown;

//     var xhr = new XMLHttpRequest();
//     xhr.open('POST', '/create_file', true);
//     xhr.setRequestHeader('Content-Type', 'text/plain');
//     xhr.send(text + ',' + tags_vulnerabilities);
// }




//  Вариант 20

// function createFile() {
//     var userInput = document.getElementById('domen_name').value;
//     var text = userInput || '33333';
//     var file = new File([text], 'domin_name.txt', {type: 'text/plain'});
//     var url = URL.createObjectURL(file);

//     var a = document.createElement('a');
//     a.href = url;
//     a.download = 'domin_name.txt';
//     a.style.display = 'none';
//     document.body.appendChild(a);

//     a.click();

//     document.body.removeChild(a);
//     URL.revokeObjectURL(url);

//     // Получение значений для всех чекбоксов
    // var cve = document.getElementById('cve').checked ? 'CVE,' : '';
    // var panel = document.getElementById('panel').checked ? 'Panel,' : '';
    // var wordpress = document.getElementById('wordpress').checked ? 'Wordpress,' : '';
    // var xss = document.getElementById('xss').checked ? 'XSS,' : '';
    // var exposure = document.getElementById('exposure').checked ? 'Exposure,' : '';
    // var wpPlugin = document.getElementById('wp-plugin').checked ? 'WP-Plugin,' : '';
    // var osint = document.getElementById('osint').checked ? 'OSINT,' : '';
    // var tech = document.getElementById('tech').checked ? 'Tech,' : '';
    // var lfi = document.getElementById('lfi').checked ? 'LFI,' : '';
    // var edb = document.getElementById('edb').checked ? 'EDB,' : '';
//     // Добавление новых чекбоксов
//     var info = document.getElementById('info').checked ? 'Info,' : '';
//     var high = document.getElementById('high').checked ? 'High' : ''; // Без запятой, т.к. последний элемент
//     var tags_vulnerabilities = cve + panel + wordpress + xss + exposure + wpPlugin + osint + tech + lfi + edb + info + high;

//     var xhr = new XMLHttpRequest();
//     xhr.open('POST', '/create_file', true);
//     xhr.setRequestHeader('Content-Type', 'text/plain');
//     xhr.send(text + ',' + tags_vulnerabilities);
// }








//  Вариант 21

// function sendDomainName() {
//     var userInput = document.getElementById('domain_name').value;
//     var xhr = new XMLHttpRequest();
//     xhr.open('POST', '/create_domain_file', true);
//     xhr.setRequestHeader('Content-Type', 'text/plain');
//     xhr.send(userInput);
// }

// function sendVulnerabilityTags() {
//     var cve = document.getElementById('cve').checked ? 'CVE,' : '';
//     var panel = document.getElementById('panel').checked ? 'Panel,' : '';
//     var wordpress = document.getElementById('wordpress').checked ? 'Wordpress,' : '';
//     var xss = document.getElementById('xss').checked ? 'XSS,' : '';
//     var exposure = document.getElementById('exposure').checked ? 'Exposure,' : '';
//     var wpPlugin = document.getElementById('wp-plugin').checked ? 'WP-Plugin,' : '';
//     var osint = document.getElementById('osint').checked ? 'OSINT,' : '';
//     var tech = document.getElementById('tech').checked ? 'Tech,' : '';
//     var lfi = document.getElementById('lfi').checked ? 'LFI,' : '';
//     var edb = document.getElementById('edb').checked ? 'EDB,' : '';
//     var tags_vulnerabilities = cve + panel + wordpress + xss + exposure + wpPlugin + osint + tech + lfi + edb;

//     var xhr = new XMLHttpRequest();
//     xhr.open('POST', '/create_tags_file', true);
//     xhr.setRequestHeader('Content-Type', 'text/plain');
//     xhr.send(tags_vulnerabilities.slice(0, -1)); // Удаляем последнюю запятую
// }

// function sendSeverity() {
//     var info = document.getElementById('info').checked ? 'Info,' : '';
//     var high = document.getElementById('high').checked ? 'High,' : '';
//     var severity = info + high;

//     var xhr = new XMLHttpRequest();
//     xhr.open('POST', '/create_severity_file', true);
//     xhr.setRequestHeader('Content-Type', 'text/plain');
//     xhr.send(severity.slice(0, -1));
// }

// Изменим HTML, чтобы использовать новые функции
// <button onclick="sendDomainName()">Send Domain Name</button>
// <button onclick="sendVulnerabilityTags()">Send Vulnerability Tags</button>
// <button onclick="sendSeverity()">Send Severity</button>







//  Вариант 22

function sendAll() {
    sendDomainName();
    sendVulnerabilityTags();
    sendSeverity();
}

function sendDomainName() {
    var userInput = document.getElementById('domain_name').value;
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/create_domain_file', true);
    xhr.setRequestHeader('Content-Type', 'text/plain');
    xhr.send(userInput);
}

function sendVulnerabilityTags() {
    var cve = document.getElementById('cve').checked ? 'CVE,' : '';
    var panel = document.getElementById('panel').checked ? 'Panel,' : '';
    var wordpress = document.getElementById('wordpress').checked ? 'Wordpress,' : '';
    var xss = document.getElementById('xss').checked ? 'XSS,' : '';
    var exposure = document.getElementById('exposure').checked ? 'Exposure,' : '';
    var wpPlugin = document.getElementById('wp-plugin').checked ? 'WP-Plugin,' : '';
    var osint = document.getElementById('osint').checked ? 'OSINT,' : '';
    var tech = document.getElementById('tech').checked ? 'Tech,' : '';
    var lfi = document.getElementById('lfi').checked ? 'LFI,' : '';
    var edb = document.getElementById('edb').checked ? 'EDB,' : '';
    var tags_vulnerabilities = cve + panel + wordpress + xss + exposure + wpPlugin + osint + tech + lfi + edb;

    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/create_tags_file', true);
    xhr.setRequestHeader('Content-Type', 'text/plain');
    xhr.send(tags_vulnerabilities.slice(0, -1)); // Удаляем последнюю запятую
}

function sendSeverity() {
    var info = document.getElementById('info').checked ? 'Info,' : '';
    var high = document.getElementById('high').checked ? 'High,' : '';
    var severity = info + high;

    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/create_severity_file', true);
    xhr.setRequestHeader('Content-Type', 'text/plain');
    xhr.send(severity.slice(0, -1));
}