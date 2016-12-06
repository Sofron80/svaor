// alert('test');
function sleep(ms) {
ms += new Date().getTime();
while (new Date() < ms){}
} 


var z = $('.form-zak');
var resize = function(){
var t = $(window).height()/2-200,
    c = $(window).width()/2-200;
    z.css({'width':'400px',
                    'height':'330px',
                    'top': t+'px',
                    'left': c+'px',
                    'opacity': 1});
}

$( window ).resize(function() {
    if (z.css('display') === 'block'){
        resize();
    }

});

$('a.button-zak').click(function(event){
    event.preventDefault();

    var temp = $('.tovar').children('h3').text();
    $('h4.zak').text(temp);
    $('.s-zak').attr('value', temp);
    z.css('display','block')
    resize();
});

// $('#submit').click(function(){
//     var data = "123098987676"
//     $.post('zakaz/', function(data) {
//         alert('агрузка завершена.');
//     });

// })
$('.closer').click(function(){
    z.css({'width':'0px',
                    'height':'0px',
                    'top': '0px',
                    'left': '0px',
                    'opacity': 0});
});

$('#form-back').submit(function(e){
    e.preventDefault();
    // var form = $(this);
    var bad = false,
        phone = $('#phone'),
        author = $('#author');


    if(author.val() === ""){
        author.addClass('form-false');
        bad = true;
    } else {
        author.addClass('form-true');
    }
    if(phone.val() === ""){
        phone.addClass('form-false');
        return false;
    } else {
        phone.addClass('form-true');
    }
    $("#status").text("Отпрвка");
    $.ajax({
        type: 'POST',
        url: '/zakaz/',
        data:{
            author: $('#author').val(),
            phone: $('#phone').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function(e){
            $('#form-back').html('<h3>Сообщение успешно отправлено</h3>');
            setTimeout(function(){
                location.reload();
            }, 2000);

        },
        error: function(){
            // console.log("ошибка");
            $("#status").text("Ошибка отправки");
        }
    });
});
