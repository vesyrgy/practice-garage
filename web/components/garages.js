import { log } from '../system/something'

/* export of function to fetch the garages */
export function get(container) {
	/**
	 * Loads the list garages
	 */
	log("loading garages");
	$.ajax({
	    type: "GET",
	    url:"/garages",
	    success: function(data) {
		    container.html(data);
	    }
	});
};