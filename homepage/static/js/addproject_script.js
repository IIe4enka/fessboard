$(document).ready(function() {
    $('#add-form-button').click(function() {
        var formsetContainer = $('#formset-container tbody');
        var lastForm = formsetContainer.find('tr:last');
        var newForm = lastForm.clone();
        newForm.find('input').val('');
        formsetContainer.append(newForm);
    });
    $(document).on('click', '.delete-form', function(){
        $(this).closest('tr').remove();
    });
});
