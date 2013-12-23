$(document).ready(function() {
	var globalArray = [];
	$.getJSON("/renderUserStocksDB").complete(function(data) {
		var jstring = data.responseText;
		if(jstring != 'Empty') {
			var jarray = JSON.parse(jstring);
			var color = 'red';
			globalArray = jarray;
			for (var i=0;i<jarray.length;i++) { 
				companyTicker = jarray[i].ticker;
				numberShares  = jarray[i].numberOfShares;
				currentPrice  = jarray[i].currentPrice;
				marketValue   = roundToTwo(currentPrice*numberShares);
				originalPrice = jarray[i].boughtAt;
				bookValue     = roundToTwo(numberShares*originalPrice);

				moneyMade 	  = roundToTwo(marketValue - bookValue);
				percentGain   = roundToTwo(((marketValue/bookValue)-1)*100);


				if(currentPrice>originalPrice) {
						color = '#008000';
				} else {
					color = 'red';
				}
				var tableRow = makeTableRows(companyTicker,moneyMade,percentGain,currentPrice,numberShares,color);
				$('#tableBody').append(tableRow);
			}
		}
	});

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

	function roundToTwo(value) {
    	return(Math.round(value * 100) / 100);
	}

	function makeTableRows(tick,moneyMade,percentGain,currentPrice,numberShares,color) {
		var row = "<tr><td style=\"color:"+color+";font-weight:bold\">"+tick+"</td>"+
							"<td style=\"color:"+color+";font-weight:bold\">"+moneyMade+"</td>"+
							"<td style=\"color:"+color+";font-weight:bold\">"+percentGain+" %</td>"+
							"<td style=\"color:"+color+";font-weight:bold\">"+currentPrice+"</td>"+
							"<td>"+numberShares+"</td></tr>";
		return row;
	}

});