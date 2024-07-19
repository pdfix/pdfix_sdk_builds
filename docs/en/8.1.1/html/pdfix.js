class PdfixDoxygenReleases {

    constructor() {
        this.appendSelectBox();
        this.appendReleasesData();
        this.onSelectBoxChange();
    }

    selectBox = '#pdfix-versions';
    documentationUrl = 'https://pdfix.github.io/pdfix_sdk_builds/en/';

    appendSelectBox() {
        let target = '#titlearea table tbody tr';
        let versionSelect = '<label for="pdfix-versions">Select another version: </label>';
        versionSelect += '<select name="pdfix-versions" id="pdfix-versions"></select>';
        let td = '<td><div style="margin-left:10px;padding:10px;">'+versionSelect+'</div></td>';
        $(target).append(td);
    }

    appendReleasesData() {
        let target = this.selectBox;
        $.ajax({
            type: 'GET',
            url: 'https://pdfix.net/wp-json/pdfix-json/v1/releases',
            dataType: 'json',
            success: function(releases, textStatus, response) {
                for ( let release of releases ) {
		    let version = release.tag_name;
		    version = version.substring(0, version.lastIndexOf(".")) 
                    $(target).append(new Option(version, version));
                }
                let version = $('#projectnumber').text();
                $(target + ' option').each(function() {
                    let optionVal = $(this).val();
                    if ( optionVal == version ) {
                        $(target).val(optionVal);
                    }
                });
            },
            failure: function(errMsg) {
                console.error(errMsg);
            },
            error: function(errMsg) {
                console.error(errMsg);
            }
        });
    }

    onSelectBoxChange() {
        let docUrl = this.documentationUrl;
        $(this.selectBox).on('change', function() {
            let version = this.value;
            let url = docUrl + version + '/html';
            location.href = url;
        });
    }

}

$( document ).ready(function() {
	new PdfixDoxygenReleases();
});
