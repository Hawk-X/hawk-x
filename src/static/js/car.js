$("#modal-car").on("submit", ".js-create-car", function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          alert("Car created!");  // <-- This is just a placeholder for now for testing
        }
        else {
          $("#modal-car .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  });