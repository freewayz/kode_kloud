/**
 * Created by peter on 6/24/16.
 *
 * Simple Ajax library for performing api operations
 * on any html forms. Implementation is based on the
 * official django-rest-framework implementation
 */


function replaceDocument(docString) {
    var doc = document.open('text/html');
    doc.write(docString);
    doc.close()
}


function doAjaxSubmit(e){
    var form = $(this); //get the current form context
    var btn = $(this.clk); //get the submit button on the form
    /*
    check for the http method verb on the
    button or form or attr element, must be
    in one of them or the default method is get
     */
    var method = btn.data('method') || form.data('method') || form.attr('method') || 'GET';
    method = method.toUpperCase();
    if (method === 'GET') {
        //GET requests can always use standard submit
        return;
    }

    var contentType  = form.find('input[data-override="content"]').val() ||
            form.find('select[data-override="content-type"] option:selected').text();

    if (method === 'POST' && !contentType) {
        //post request can use standard form submit unless we have overriden the the content type
        return;
    }

    //at this point we need to make AJAX Form submission
    e.preventDefault();

    var url  = form.attr('action');
    var data;

    if (contentType) {
        data = form.find('[data-override="content"]').val() || '';
    } else {
        contentType = form.attr('enctype') || form.attr('encoding');

        if (contentType === 'multipart/form-data') {
            if (!window.FormData) {
                alert("Upgrade browser. File upload not supported");
                return;
            }

            contentType = false;
            data = new FormData(form[0]);
        } else {
            contentType = 'application/x-www-form-urlencoded; charset=UTF-8';
            data = form.serialize();
        }
    }


    var ret = $.ajax({
        url : url,
        method : method,
        data : data,
        contentType : contentType,
        processData : false,
        headers : {'Accept': 'text/html; q=1.0, */*'}
    });

     ret.always(function(data, textStatus, jqXHR) {
        if (textStatus != 'success') {
            jqXHR = data;
        }
        var responseContentType = jqXHR.getResponseHeader("content-type") || "";
        if (responseContentType.toLowerCase().indexOf('text/html') === 0) {
            replaceDocument(jqXHR.responseText);
            try {
                // Modify the location and scroll to top, as if after page load.
                history.replaceState({}, '', url);
                scroll(0,0);
            } catch(err) {
                // History API not supported, so redirect.
                window.location = url;
            }
        } else {
            // Not HTML content. We can't open this directly, so redirect.
            window.location = url;
        }
    });
    return ret;

}

function captureSubmittingElement(e) {
    var target = e.target;
    var form = this;
    form.clk = target;
}


$.fn.ajaxForm = function() {
    var options = {};
    return this
        .unbind('submit.form-plugin  click.form-plugin')
        .bind('submit.form-plugin', options, doAjaxSubmit)
        .bind('click.form-plugin', options, captureSubmittingElement);
};
