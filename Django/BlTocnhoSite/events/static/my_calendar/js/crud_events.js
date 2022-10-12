var doFunction = function(action){
var areUsure = confirm("Вы уверены что хотите "+action + " ?");
if (areUsure) {
   var id = document.getElementById("event_id").textContent
   console.log(id)
} else {
   console.log('Пошел впизду')
}
// 1. Создаём новый объект XMLHttpRequest
//var xhr = new XMLHttpRequest();
//
//// 2. Конфигурируем его: GET-запрос на URL 'phones.json'
//xhr.open('GET', 'phones.json', false);
//
//// 3. Отсылаем запрос
//xhr.send();
//
//// 4. Если код ответа сервера не 200, то это ошибка
//if (xhr.status != 200) {
//  // обработать ошибку
//  alert( xhr.status + ': ' + xhr.statusText ); // пример вывода: 404: Not Found
//} else {
//  // вывести результат
//  alert( xhr.responseText ); // responseText -- текст ответа.
//}
}

document.getElementById("succes_button").onclick = function() { doFunction('Выполненно'); };
document.getElementById("no_succes_button").onclick = function() { doFunction('Не Выполненно'); };
document.getElementById("pending_button").onclick = function() { doFunction('Перенести евент'); };
document.getElementById("cancel_button").onclick = function() { doFunction('Отменено'); };
