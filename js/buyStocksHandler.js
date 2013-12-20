$(document).ready(function() {
	// $(".sidebar-app p").removeClass("active")
	// $("#buyLinkName").addClass("active");
	$("#querystockbutton").click(function() {
		$('#querystockbutton').attr('disabled', 'disabled');
		var quoteToSearch = $("#priceSearchInput").val().toUpperCase();
		$.getJSON("/getPrice/"+quoteToSearch).complete(function(data) {
			var response = String(data.responseText);
			if(response == 'Error') {
				alert('There was an error, please try again');
			} else {
				$("#retriedStockHolder").show();
				$("#priceRetrieved").val("Price : $"+response);
				$("#priceSearchInput").val(quoteToSearch);
				$("#tickerInput").val(quoteToSearch);
			}
			$('#querystockbutton').removeAttr('disabled');
		});
	});

	$("#buystocksbutton").click(function() {
		$('#buystocksbutton').attr('disabled', 'disabled');
		var ticker = $("#tickerInput").val();
		var numberOfShares = $("#quantitySharesInput").val()
		if(getInt(numberOfShares) != 'wrong' && numberOfShares > 0) {
			$.getJSON("/render/"+ticker.toUpperCase()+"/"+numberOfShares).complete(function(data) {
				loadedValues = data.responseText;
				var response = String(loadedValues);
	
					if(response == 'Error') {
						alert('There was an error, please try again');
					} 
					else if(response == 'NotEnoughCash') {
						alert('Not enough cash available for transaction');
					}
					else {
						window.location.href = "/";
					}
					$('#buystocksbutton').removeAttr('disabled');
			});
		} else {
			alert('Please enter a proper number');
			$('#buystocksbutton').removeAttr('disabled');
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