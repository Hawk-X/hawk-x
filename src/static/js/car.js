$(function () {

  $(".js-create-car").click(function () {
    $.ajax({
      url: '/shop/create/',
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-car").modal("show");
      },
      success: function (data) {
        $("#modal-car .modal-content").html(data.html_form);
      }
    });
  });

});
