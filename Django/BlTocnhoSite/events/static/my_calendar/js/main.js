//var Calendar_builder = function(divId) {
//    //Сохраняем идентификатор div
//    this.divId = divId;
//    // Дни недели с понедельника
//    this.DaysOfWeek = [
//      'Пн',
//      'Вт',
//      'Ср',
//      'ЧТ',
//      'ПТ',
//      'СБ',
//      'ВС'
//    ];
//    // Месяцы начиная с января
//    this.Months =['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'];
//    //Устанавливаем текущий месяц, год
//    var today = new Date();
//    this.currMonth = today.getMonth();
//    this.currYear = today.getFullYear();
//    this.currDay = today.getDate();
//  };
//  // Переход к следующему месяцу
//  Calendar_builder.prototype.nextMonth = function() {
//    if ( this.currMonth == 11 ) {
//      this.currMonth = 0;
//      this.currYear = this.currYear + 1;
//    }
//    else {
//      this.currMonth = this.currMonth + 1;
//    }
//    this.showcurr();
//  };
//  // Переход к предыдущему месяцу
//  Calendar_builder.prototype.previousMonth = function() {
//    if ( this.currMonth == 0 ) {
//      this.currMonth = 11;
//      this.currYear = this.currYear - 1;
//    }
//    else {
//      this.currMonth = this.currMonth - 1;
//    }
//    this.showcurr();
//  };
//  // Показать текущий месяц
//  Calendar_builder.prototype.showcurr = function() {
//    this.showMonth(this.currYear, this.currMonth);
//  };
//  // Показать месяц (год, месяц)
//  Calendar_builder.prototype.showMonth = function(year,month) {
//    var calendar_template='';
//    start_day=new Date(this.currYear,this.currMonth,1);
//    end_date=new Date(this.currYear,this.currMonth+1,0);
//    start_day.setDate(start_day.getDate() - start_day.getDay()+1);
//    var month=''
//    while (start_day<=end_date){
//        var week=['','','','','','','']
//        for (let index = 0; index < 7; index++) {
//            if (start_day.getDay()==0){
//                week[6]=`<div class="col">${start_day}</div>`
//                break
//            } else{
//                week[start_day.getDay()-1]=`<div class="col">${start_day}</div>`
//                start_day.setDate(start_day.getDate() + 1);
//                continue
//            };
//        }
//        week=week.join('');
//        week=`<div class="row">${week}</div>`;
//        month+=week;
//        start_day.setDate(start_day.getDate() + 1);
//    }
//    calendar_template+=month
//    calendar_template+='</div>'
//    console.log(calendar_template)
//    document.getElementById(this.divId).innerHTML = calendar_template;
//  };
//
//  // При загрузке окна
//window.onload = function() {
//// Начать календарь
//var calendar = new Calendar_builder("divCal");
//calendar.showMonth();
//
//getId('btnNext').onclick = function() {
//    calendar.nextMonth();
//};
//getId('btnPrev').onclick = function() {
//    calendar.previousMonth();
//};
//}
//// Получить элемент по id
//function getId(id) {
//    return document.getElementById(id);
//}