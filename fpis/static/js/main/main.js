
$(document).ready(function(){
    // AJAX GET
    $('.get-more').click(function(){
        $.ajax({
            type: "GET",
            url: "/main/ajax/more/",
            success: function(data){
                for(i = 0; i < data.length; i++){
                    $('ul').append('<li>' + data[i] + '</li>')
                }
            }
        });
    });

    // AJAX POST
    $('.add-todo').click(function(){
        $.ajax({
            type: "POST",
            url: "/main/ajax/add/",
            dataType: "json",
            data: {"item": $(".todo-item").val()},
            success: function(data){
                alert("nihao");
            }
        });
    });

    // CSRF code
    // using jQuery
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');
    });

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });