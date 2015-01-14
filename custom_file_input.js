$(document).ready(function () {
    var inputs_file = $("[class='custom_file_input']input[type='file']");
    var count_inputs = 1;
    inputs_file.each(function () {
        var input_origin = $(this);
        input_origin.attr('data-custom-id', count_inputs);
        input_origin.hide();
        input_origin.after('<div class="group_clear new_custom_input_file">' +
        '<button type="button" id="custom_file_input_' + count_inputs + '" class="button_default btn-blue float_left">Escolher arquivo</button>' +
        '<label id="custom_file_label_' + count_inputs + '" for="custom_file_input_' + count_inputs + '">Nenhum arquivo selecionado</label>' +
        '</div>');
        var new_element = $("#custom_file_input_" + count_inputs);
        new_element.click(function () {
            input_origin.click();
        });
        input_origin.change(function () {
            var file_name = input_origin.val();
            var number = input_origin.attr('data-custom-id');
            $("#custom_file_label_" + number).text(file_name.split('\\')[file_name.split('\\').length - 1]);
        });
        count_inputs++;
    });
});
