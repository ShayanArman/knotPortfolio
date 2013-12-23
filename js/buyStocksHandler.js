$(document).ready(function() {
	var sharePrice;
	var percent = ((($("#cashVal").text())/100000)*100)*2;
	$(".cash_inner_container").css("width",percent);

	$("#querystockbutton").click(function() {
		$('#querystockbutton').attr('disabled', 'disabled');
		var quoteToSearch = $("#priceSearchInput").val().toUpperCase();
		$.getJSON("/getPrice/"+quoteToSearch).complete(function(data) {
			var sharePrice = String(data.responseText);
			if(sharePrice == 'Error') {
				alert('There was an error, please try again');
			} else {
				$("#retrievedStockHolder").show();
				$("#priceRetrieved").val("Price : $"+sharePrice);
				$("#priceSearchInput").val(quoteToSearch);
				$("#tickerInput").val(quoteToSearch);
			}
			$('#querystockbutton').removeAttr('disabled');
		});
	});

    $('#quantitySharesInput').keyup(function(event) {
        var numberSharesDog = $(this).val();
        var pricePerShare = $("#priceRetrieved").val();
        pricePerShare = parseFloat(pricePerShare.substring(9,pricePerShare.length));
        if(pricePerShare) {
        	$('#mirrorInput').val("$ " + (numberSharesDog*pricePerShare));
        }
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