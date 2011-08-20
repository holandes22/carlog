$(document).ready(
	function() {
		$( "#navbar_car_index" ).button({
			icons: {
				primary: "ui-icon-home"
			}
		});		
		$( "#navbar_treatment_index, #navbar_mechanic_index" ).button();
		$( "#navbar_search" ).button({
			icons: {
				primary: "ui-icon-search"
			}
		});
		$( "#navbar_account" ).button({
			icons: {
				primary: "ui-icon-person"
			}
		});
		$( "#navbar_logout" ).button({
			text: false,
			icons: {
				primary: "ui-icon-power"
			}
		});				
	}
);
