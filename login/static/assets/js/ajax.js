$(function(){

    $('#button').click(function() {
    
        $.ajax({
            type: "POST",
            url: "search",
            data: { 
                'search_text_first' : $('#search_first').val(),
                'search_text_last' : $('#search_last').val(),
                'search_id' : $('#search_id').val(),
                'search_gend' : $('#search_gender').val(),
                'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
            },
            success: searchSuccess,
            dataType: 'html'
        });
    });
});

function searchSuccess(data, textStatus, jqXHR)
{ 
    $('#search-results').html(data);
}