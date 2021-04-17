/* переопределить поведение кнопки "Отправить" */
$(document).ready(function () {
    $("#contact-form").submit(function (event) {
        event.preventDefault();
        sendAjaxForm("contact-form", "msg");
    });
});

/* отправка формы через ajax */
function sendAjaxForm(form_ajax, msg) {
    let form = $("#" + form_ajax);
    $.ajax({
        type: form.attr('method'),
        url: form.attr('action'),
        data: form.serialize(),
        success: function (response) {
            let json = jQuery.parseJSON(response);
            $("#" + msg).html(json.msg);
            if (json.success === 'true') {
                form.trigger('reset');
                setTimeout(function () {
                    $("#" + msg).html('');
                }, 5000);
            }
            else {
                $("#" + msg).html(json.msg);
                console.log('Some error, check all fields, please');
            }
        },
        error: function (error) {
            console.log(error);
        }
    });
}