// >>>> Public key input >>>>

$("input[id='public_key']").on("focus", function () {
    $(this).select();
});

// <<<< <<<<
// >>>> Download function >>>>
function downloadFile(download_link) {
    // AJAX requests to backend to download file by external link
    $.ajax({
        url: $(location).attr("href"),
        method: "post",
        xhrFields: {
            responseType: "blob",
        },
        data: {
            csrfmiddlewaretoken: $("meta[name='csrf-token']").attr("content"),
            download_link: download_link,
        },
        success: function (data, status, xhr) {
            // Extract filename from Content-Disposition header
            let filename = "";
            let disposition = xhr.getResponseHeader("Content-Disposition");
            if (disposition && disposition.indexOf("attachment") !== -1) {
                let filenameRegex = /filename[^;=\n]*=((['"]).*?\2|[^;\n]*)/;
                let matches = filenameRegex.exec(disposition);
                if (matches != null && matches[1]) {
                    filename = matches[1].replace(/['"]/g, "");
                }
            }

            // Create a link to download the file and click it
            let blob = new Blob([data], {
                type: xhr.getResponseHeader("Content-Type"),
            });
            let link = $("<a>", {
                href: window.URL.createObjectURL(blob),
                download: filename,
            });
            link[0].click();
        },
    });
}

// <<<< <<<<
// >>>> Row download button >>>>

function downloadFileButton() {
    // Downloads the file specified in the row
    downloadFile($(this).attr("download_link"));
}
$(".download-file-button").click(downloadFileButton);

// <<<< <<<<
// >>>> Download checkboxes >>>>

let current_dir_checkbox = $("#download-file-checkbox-current-dir");
let files_checkboxes = $(".download-file-checkbox");

function toggleAllCheckbox() {
    // Checks all checkbox if the current_dir_checkbox is checked and vice versa
    files_checkboxes.prop("checked", current_dir_checkbox.is(":checked"));
}
current_dir_checkbox.change(toggleAllCheckbox);

function toggleCurrentDirCheckbox() {
    // Checks the current_dir_checkbox if all checkbox is checked and vice versa
    let check_current_dir_checkbox = true;

    files_checkboxes.each(function (index, element) {
        check_current_dir_checkbox =
            check_current_dir_checkbox & element.checked;
    });

    current_dir_checkbox.prop("checked", check_current_dir_checkbox);
}
files_checkboxes.change(toggleCurrentDirCheckbox);

function downloadFileCheckboxes() {
    // Download all checked files or current dir, if checked
    if (current_dir_checkbox.is(":checked")) {
        downloadFile(current_dir_checkbox.attr("download_link"));
    } else {
        files_checkboxes.each(function (index, element) {
            if (element.checked) {
                downloadFile($(element).attr("download_link"));
            }
        });
    }
}
$(".download-file-checkbox-button").click(downloadFileCheckboxes);

// <<<< <<<<
// >>>> Filter types >>>>

function filesTypeFilter() {
    let selected_type = $("#files-type-filter option:selected").attr("value");

    if (selected_type == "all") {
        $(".table-files-row").show();
    } else {
        $(".table-files-row").each(function () {
            if ($(this).attr("row_type") == selected_type) {
                $(this).show();
            } else {
                $(this).hide();
            }
        });
    }
}
$("#files-type-filter").on("change", filesTypeFilter);

// <<<< <<<<
