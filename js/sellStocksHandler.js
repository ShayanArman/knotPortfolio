$(document).ready(function() {
	$("#sellstocksbutton").click(function() {
		$('#sellstocksbutton').attr('disabled', 'disabled');
		var ticker = $("#tickerSell").val();
		var numberOfShares = $("#numberSharesSell").val();
		if(getInt(numberOfShares) != 'wrong' && numberOfShares > 0) {
			$.getJSON("/sell/"+ticker.toUpperCase()+"/"+numberOfShares).complete(function(data) {
				var response = String(data.responseText);
	
					if(response == 'moreSharesThanYouHaveError') {
						alert('You are trying to sell more shares than you own!');
					} else {
						var alertString = "You made " + response + " dollars! This will be added to your cash balance";
						alert(alertString);
						window.location.href = "/";
					}
					$('#sellstocksbutton').removeAttr('disabled');
				});
		} else {
			alert('Please enter a proper number');
			$('#sellstocksbutton').removeAttr('disabled');
		}
	
	});

	function getInt(x) {
	    if (typeof x !== "number" && typeof x !== "string" || x === "") {
	        return 'wrong';
	    } else {
	        x = Number(x);
	        return x === Math.floor(x) ? x : 'wrong';
	    }
	}

});