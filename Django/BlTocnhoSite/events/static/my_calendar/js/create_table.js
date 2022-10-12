var tableCreate = function tableCreate() {
    var date_string = document.getElementById("date_string").textContent

    var xhr = new XMLHttpRequest();
    xhr.open('GET', 'http://127.0.0.1:8000/api/events/', false);
    xhr.send();
    if (xhr.status != 200) {
        console.log(xhr.status)
    } else {
        var events = JSON.parse(xhr.responseText);
        const result = events.filter(event_dict => event_dict.dt == date_string);
        console.log(result)
        var body = document.getElementsByTagName("body")[0];
        var tbl = document.createElement("table");
        tbl.classList.add("day_table")
        var tblBody = document.createElement("tbody");
        // cells creation
        for (var j = 0; j < result.length; j++) {
        // table row creation
            var row = document.createElement("tr");
            row.classList.add("my_row")
            var cell_counter = document.createElement("td");
            cell_counter.classList.add("event_col")
            cell_counter.classList.add("counter")
            var counter = j+1
            var cell_counter_Text = document.createTextNode("#" + counter);
            cell_counter.appendChild(cell_counter_Text);
            row.appendChild(cell_counter);

            var cell_tm = document.createElement("td");
            cell_tm.classList.add("event_col")
            cell_tm.classList.add("tm")
            var tm = result[j].tm;
            var cell_counter_tm = document.createTextNode(tm);
            cell_tm.appendChild(cell_counter_tm);
            row.appendChild(cell_tm);

            var cell_name = document.createElement("td");
            cell_name.classList.add("event_col")
            cell_name.classList.add("name")
            var name = result[j].name;
            var cell_name_text = document.createTextNode(name);
            cell_name.appendChild(cell_name_text);
            row.appendChild(cell_name);

            var cell_category = document.createElement("td");
            cell_category.classList.add("event_col")
            cell_category.classList.add("category")
            var category = result[j].category;
            var cell_category_text = document.createTextNode(category);
            cell_category.appendChild(cell_category_text);
            row.appendChild(cell_category);

            var cell_desc = document.createElement("td");
            cell_desc.classList.add("event_col")
            cell_desc.classList.add("desc")
            var desc = result[j].desc;
            var cell_desc_text = document.createTextNode(desc);
            cell_desc.appendChild(cell_desc_text);
            row.appendChild(cell_desc);
            tblBody.appendChild(row);
        }

        // append the <tbody> inside the <table>
        tbl.appendChild(tblBody);
        // put <table> in the <body>
        body.appendChild(tbl);

    }

}

tableCreate()