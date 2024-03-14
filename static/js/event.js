$(function(){
  var loadForm = function(){
      var btn = $(this);
      $.ajax({
          url: btn.attr("data-url"),
          type: 'get',
          dataType: 'json',
          beforeSend: function(){
              $("#modal-form").modal("show");
          },
          success: function(data){
              $("#modal-form .modal-content").html(data.html_form);
          }
      });
  };
  var saveForm = function(){
      var form = $(this);
      $.ajax({
          url: form.attr("action"),
          data: form.serialize(),
          type: form.attr("method"),
          dataType: 'json',
          success: function(data){
              if(data.form_is_valid){
                  $("#table-json tbody").html(data.html_list);
                  $("#modal-form").modal("hide");
                  if(data.html_pagination){
                    $("#pagination").html(data.html_pagination);
                  }
              }
              else{
                  $("#modal-form .modal-content").html(data.html_form)
              }
          }
      });
      return false
  };
 
  // CREATE
  $(".js-create").click(loadForm);
  $("#modal-form").on("submit", ".js-create-form", saveForm);

  // UPDATE
  $("#table-json").on("click", ".js-update", loadForm);
  $("#modal-form").on("submit", ".js-update-form", saveForm);

  // DELETE
  $("#table-json").on("click", ".js-delete", loadForm);
  $("#modal-form").on("submit", ".js-delete-form", saveForm); 
});