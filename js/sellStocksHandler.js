$(document).ready(function() {
	var stockPriceDictionary = {};

	$.getJSON("/renderUserStocksDB").complete(function(data) {
		var jstring = data.responseText;
		if(jstring != 'Empty') {
			var jarray = JSON.parse(jstring);
			var color = 'red';
			for (var i=0;i<jarray.length;i++) { 
				companyTicker = jarray[i].ticker;
				numberShares  = jarray[i].numberOfShares;
				currentPrice  = jarray[i].currentPrice;
				marketValue   = roundToTwo(currentPrice*numberShares);
				originalPrice = jarray[i].boughtAt;
				bookValue     = roundToTwo(numberShares*originalPrice);

				moneyMade 	  = roundToTwo(marketValue - bookValue);
				percentGain   = roundToTwo(((marketValue/bookValue)-1)*100);

				stockPriceDictionary[companyTicker] = currentPrice;

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

	$('#numberSharesSell').keyup(function(event) {
        var numberSharesDog = $('#numberSharesSell').val();
        rightFormat = (getInt(numberSharesDog) != 'wrong');
        numberGreaterThanZero = (numberSharesDog > 0);
        ticker = $("#tickerSell").val().toUpperCase();
        goodSharePrice = stockPriceDictionary[ticker];

        if(goodSharePrice && rightFormat && numberGreaterThanZero) {
        	setMirrorInput("$ " + (numberSharesDog*goodSharePrice).toFixed(2));
        } 
        else if(!goodSharePrice && rightFormat && numberGreaterThanZero) {
        	setMirrorInput("Enter A Stock You Own");
        	setTimeout(function() { enterStockSymbolAndUpdatePrice();},3500);
        }
        else if(!rightFormat && numberSharesDog != "") {
        	setMirrorInput("Enter A Proper Number");
        }
        else if(numberSharesDog == 0) {
        	setMirrorInput("$ 0.00");	
        }
    });

	$("#sellstocksbutton").click(function() {
		$('#sellstocksbutton').attr('disabled', 'disabled');
		var ticker = $("#tickerSell").val().toUpperCase();
		var numberOfShares = $("#numberSharesSell").val();
		if(getInt(numberOfShares) != 'wrong' && numberOfShares > 0) {
			$.getJSON("/sell/"+ticker.toUpperCase()+"/"+numberOfShares).complete(function(data) {
				var response = String(data.responseText);
	
					if(response == 'moreSharesThanYouHaveError') {
						if(stockPriceDictionary[ticker]) {
							setMirrorInput('Enter Less Shares');
						} else {
							setMirrorInput('Enter A Stock You Own');
						}
					} else {
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

	function enterStockSymbolAndUpdatePrice() {
		var numberSharesDog = $('#numberSharesSell').val();
        rightFormat = (getInt(numberSharesDog) != 'wrong');
        numberGreaterThanZero = (numberSharesDog > 0);
        ticker = $("#tickerSell").val().toUpperCase();
        goodSharePrice = stockPriceDictionary[ticker];
    	

    	if(goodSharePrice && rightFormat && numberGreaterThanZero) {
        	setMirrorInput("$ " + (numberSharesDog*goodSharePrice).toFixed(2));
        } 
	}

	/*  Change the total cost input to represent the total cost or the warning terms  */
	function setMirrorInput(totalCost) {
		$('#mirrorInput').val(totalCost);
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