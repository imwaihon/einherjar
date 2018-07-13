(function() {

setTimeout(function() {
	function getScores(text) {
		document.getElementById('rest').style.display = 'none';
		document.getElementById('result').style.display = 'none';
		document.getElementById('loading').style.display = 'block';
		axios.post('http://localhost:5000/parse', {
			textPayload: text
		}).then(function (response) {
			document.getElementById('result').style.display = 'block';
			document.getElementById('loading').style.display = 'none';
			console.log(response);
		})
		.catch(function (error) {
			document.getElementById('rest').style.display = 'block';
			document.getElementById('loading').style.display = 'none';
			console.log(error);
		});
	}

	const elements = document.getElementsByClassName('tryButton');
	console.log(elements[0]);
	if (elements.length > 0) {
		elements[0].addEventListener('click', function(event) {
			event.preventDefault();
			getScores('Most Singapore Ministers agrees with MOE implementation of parking fees for teachers');
		}, true);
	}
}, 1000);

})();