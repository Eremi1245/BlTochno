var tableCreate = function tableCreate() {
    while (True) {
        var one_hour_seconds=3600
        var today=new Date()
        var hour=today.getHours()
        var minute=today.getMinutes()
        var second=today.getSeconds()
        var margin_element=(one_hour_seconds*(hour+minute/100+second/100)*100)/86400
        $('#current_time').css('margin-left', margin_element);
    }

}

tableCreate()