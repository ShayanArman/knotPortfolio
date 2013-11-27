$(document).ready(function() {
	$("#portfolioLinkName").css("color","#8580F7");
	// $("#portfolioButton").css("color","#8580F7");
	//$(".sidebar-app p#portfolioLinkName").addClass("active")
	$.getJSON("/renderUserStocksDB").complete(function(data) {
			var jstring = data.responseText;
			if(jstring != 'Empty') {
				var jarray = JSON.parse(jstring);
				var color = 'red';
				for (var i=0;i<jarray.length;i++) { 
					companyTicker = jarray[i].ticker;
					numberShares  = jarray[i].numberOfShares;
					currentPrice  = jarray	[i].currentPrice;
					marketValue   = currentPrice*numberShares;
					marketValue   = Math.round(marketValue * 100)/100;
					originalPrice = jarray[i].boughtAt;
					bookValue     = numberShares*originalPrice;
					bookValue     = Math.round(bookValue * 100)/100;
					if(currentPrice>originalPrice) {
							color = '#008000';
					} else {
						color = 'red';
					}
					var tableRow = makeTableRows(companyTicker,marketValue,bookValue,originalPrice,currentPrice, color);
					$('#tableBody').append(tableRow);
				}
			}
	});

	
	function makeTableRows(tick,marketVal,bookVal,originalPrice,currentPrice,color) {
		var row = "<tr><td style=\"color:"+color+";font-weight:bold\">"+tick+"</td>"+
							"<td>"+bookVal+"</td>"+
							"<td style=\"color:"+color+";font-weight:bold\">"+marketVal+"</td>"+
							"<td>"+originalPrice+"</td>"+
							"<td style=\"color:"+color+";font-weight:bold\">"+currentPrice+"</td></tr>";
		return row;
	}

});