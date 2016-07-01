    
    
var dialog, form;
dialog = $('#create-todo-form').dialog({
    autoOpen: false,
    height: 300,
    width: 300,
    modal: true

});

 $("#create-todo").button().on("click", function() {
     dialog.dialog('open');
 })




function showVal (result) {
    var hData = {'yourName' : result}
    var theTemplateScript = $('#testing').html()
    alert(theTemplateScript)
    var theTemplate = Handlebars.compile(theTemplateScript)
    $(document.body).append(theTemplate(hData));
    alert("data")
    
}


$("#btn").button().on("click", function() {
    form = $('#todo-form');
    var url = form.attr('action');
    $.post(url, form.serialize(), function(data) {
        showVal("Peter saved")
    });
    
});

    