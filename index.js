indexMap = {"search":""}; // 'Maps' list from database to objects in javascript
page_loads = 0; // Tracks how many times the page has been loaded

// Search function
function filter(data) {

    var input = document.getElementById('search');
    if (page_loads == 1 && window.location.hash != "") {
        var search = window.location.hash.split("#")[1];
    }
    else{
        if (input == "") {
            window.location.hash = "";
        }
        var search = input.value;
        window.location.hash = search;
    }
    indexMap["search"] = search;

    return;
}

// Highlights letters that have been searched
function highlight_search(name) {
    var new_search = indexMap["search"];
    var new_split = name.split(new_search);
    var new_name = "";
    var html_name = "";

    for (var l = 0; l < new_split.length; l++) {
        new_name += new_split[l];
        html_name += new_split[l];
        if (name.indexOf(new_name + new_search) != -1) {
            new_name += new_search;
            html_name += "<font class='bg-success'>"+new_search+"</font>";
        }
    }

    return html_name;
}

function load_page() {

    page_loads += 1;
    filter();

    $.getJSON("database.json", function(data) {
        var to_append = ""; // to store string of html to append to ul
        var div = $("#main_list"); // points to the 'div' (division) html element
        div.html(""); // clear all html contained by <div></div>
        search = indexMap["search"];
        var results_exist = false;
        $.each(data, function(key, val) {
            if (val["name"].indexOf(search) >= 0) {
                results_exist = true;
                var html_name = highlight_search(val["name"]);

                to_append += "<div class'container' id='"+key+"'><hr><p><h4>"+html_name+
                             "</h2><b>File: </b>"+val["file"]+
                             "<br /><b>Observer: </b>"+val["observer"]+
                             "<br /><b>Filter: </b>"+val["filter"]+"</p><hr></div>";
            }
        });
        if (results_exist == false) {
            div.append("<div class='container text-center'><p>No entries matching '"+search+"' exist.</p></div>")
        }
        div.append(to_append);
    });

}

// Main function
$(function() {
    console.log(localStorage);

    load_page();

    // Initital hides
    $("#load").hide();
    $("#load_msg").hide();
    $("#finished").hide();
    $("#input_err").hide();
    $("#internal_err").hide();
    $("#SingleMuon").hide();
    $("#Cosmics").hide();

    // Initial Disables
    $("#submit").attr('disabled', 'disabled');

    // Prevent 'enter' key from submitting forms (gives 404 error with full data set name form)
    $(window).keydown(function(event) {
        if (event.keyCode == 13) {
            event.preventDefault();
            return false;
        }
    });

});
