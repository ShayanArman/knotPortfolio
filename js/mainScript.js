var doneRequest = 0; // Semaphore.
$(document).ready(function() {
	$("#jsonContainer").load("/renderUserStocksDB", function() {
			var jstring = $("#jsonContainer").html();
			if(jstring != 'Empty') {
				var jarray = JSON.parse(jstring);
				for (var i=0;i<jarray.length;i++) { 
					companyTicker = jarray[i].ticker;
					numberShares  = jarray[i].numberOfShares;
					currentPrice  = jarray[i].currentPrice;
					marketValue   = currentPrice*numberShares;
					marketValue   = Math.round(marketValue * 100)/100;
					originalPrice = jarray[i].boughtAt;
					bookValue     = numberShares*originalPrice;
					bookValue     = Math.round(bookValue * 100)/100;
	
					$('#tableBody').append("<tr><td>"+companyTicker+"</td><td>"+originalPrice+"</td><td>"+bookValue+"</td><td>"+marketValue+"</td><td>"+currentPrice+"</td></tr>");
				}
			} else {
				alert(jstring);
			}
	});
	
	$("#addStockButton").click(function() {
		$('#addStockButton').attr('disabled', 'disabled');
		var ticker = $("#tickerInput").val();
		var numberOfShares = $("#numberOfSharesInput").val();
		
			$("#ajaxValue").load("/render/"+ticker.toUpperCase()+"/"+numberOfShares, function() {

				loadedValues = $("#ajaxValue").html();
				var response = String(loadedValues);
	
					if(response == 'Error') {
						alert('There was an error, please try again');
					} 
					else if(response == 'NotEnoughCash') {
						alert('Not enough cash available for transaction');
						doneRequest = 0;
					}
					else {
						doneRequest = 0;

						ajaxValuesArray = loadedValues.split("~");
		
						numberOfShares = ajaxValuesArray[2];
		
						companyTicker = ajaxValuesArray[0];
						currentPrice  = ajaxValuesArray[1];
						marketValue   = currentPrice*numberOfShares;
						marketValue   = Math.round(marketValue*100)/100;
						originalPrice = currentPrice;
						originalPrice = Math.round(originalPrice*100)/100;
						bookValue     = numberOfShares*currentPrice;
						bookValue     = Math.round(bookValue*100)/100;
						
						$('#tableBody').append("<tr><td>"+companyTicker+"</td><td>"+originalPrice+"</td><td>"+bookValue+"</td><td>"+marketValue+"</td><td>"+currentPrice+"</td></tr>");
	
						doneRequest = 0;
					}
					$('#addStockButton').removeAttr('disabled');
				});
		
	
	});

});