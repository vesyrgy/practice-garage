import 'bootstrap';
import * as garages from './components/garages'

$(function() {
	/****
	 * $(function() <code>)}
	 * contains code that will be executed when page is loaded
	 */
	garages.get($('#garage-list'))
});