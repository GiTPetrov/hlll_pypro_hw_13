$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-contact .modal-content").html("");
        $("#modal-contact").modal("show");
      },
      success: function (data) {
        $("#modal-contact .modal-content").html(data.html_form);
      }
    });
  };


  var sendForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("data-url"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
//      beforeSend: function () {
//        $("#modal-contact .modal-content").html("");
//        $("#modal-contact").modal("show");
//      },
      success: function (data) {
        if (data.form_is_valid) {
          $("#modal-contact .modal-content").html(data.form_sent);
//          $("#modal-contact").modal("hide");
        }
        else {
          $("#modal-contact .modal-content").html(data.form_sent);
        }
      }
    });
    return form;
  };



//  var sendForm = function () {
//    var form = $(this);
//    $.ajax({
//      url: form.attr("action"),
//      data: form.serialize(),
//      type: form.attr("method"),
//      dataType: 'json',
//      success: function (data) {
//        if (data.form_is_valid) {
//          $("#modal-contact").modal("hide");
//        }
//        else {
//          $("#modal-contact .modal-content").html(data.form_sent);
//        }
//      }
//    });
//    return false;
//  };


  /* Binding */

  // Create message
  $(".js-contact-us").click(loadForm);
//    $("#modal-contact .js-send-message").click(sendForm);
  $("#modal-contact").click("input", ".js-message-create-form", sendForm);


});
