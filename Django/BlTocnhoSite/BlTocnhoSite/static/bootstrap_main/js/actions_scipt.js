$("#datatablesSimple").submit(function(e){
    e.preventDefault();
    console.log(e)
    var values=e.target.lastElementChild.attributes[0].value.split(' ')
    $.ajax({
        type : 'POST',
        url :  "{% url 'event_action' %}",
        contentType: 'application/json',
        headers : {"X-CSRFToken": '{{ csrf_token }}'},
        dataType: 'json',
        data : {
          'id':values[0],
          'action':values[1],
          'csrfmiddlewaretoken': '{{ csrf_token }}'
        },
        success : function(response){
                var event_id='#event_'+values[0]
                var status_id='#status_'+values[0]
                var actions_id='#actions_'+values[0]
                console.log(event_id)
                console.log(status_id)
                if (values[1]=='SUCCES'){
                  $(event_id).css('background-color', 'greenyellow').css('opacity','0.4');
                  $(status_id).text('Успешно выполненное');
                  // $(actions_id).html("");
                }
                else if(values[1]=='NO_SUCCES'){
                  $(event_id).css('background-color', 'indianred').css('opacity','0.4');
                  $(status_id).text('Не выполненное');
                }
                else if(values[1]=='PENDING'){
                  $(event_id).css('background-color', 'rgb(201, 231, 144)').css('opacity','0.4');
                  $(status_id).text('Отложенное');
                }
                else if(values[1]=='CANCEL'){
                  $(event_id).css('background-color', 'grey').css('opacity','0.4');
                  $(status_id).text('Отмененно');
                }

        },
        error : function(response){
            console.log(response)
        }
    });
});