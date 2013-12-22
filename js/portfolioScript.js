$(document).ready(function() {
	var percent = ((($("#cashVal").text())/100000)*100)*2;
	$(".cash_inner_container").css("width",percent);

	$.getJSON("/renderUserStocksDB").complete(function(data) {
			var jstring = data.responseText;
			var totalMarketPosition = 0;
			if(jstring != 'Empty') {
				var jarray = JSON.parse(jstring);
				var color = 'red';
				for (var i=0;i<jarray.length;i++) { 
					companyTicker = jarray[i].ticker;
					numberShares  = jarray[i].numberOfShares;
					currentPrice  = jarray[i].currentPrice;
					marketValue   = currentPrice*numberShares;
					marketValue   = Math.round(marketValue * 100)/100;
					totalMarketPosition += marketValue;
					originalPrice = jarray[i].boughtAt;
					bookValue     = numberShares*originalPrice;
					bookValue     = Math.round(bookValue * 100)/100;
					percentGain   = (((marketValue/bookValue)-1)*100).toFixed(2);

					if(currentPrice>originalPrice) {
							color = '#008000';
					} else {
						color = 'red';
					}
					var tableRow = makeTableRows(companyTicker,marketValue,bookValue,originalPrice,currentPrice,percentGain,color);
					$('#tableBody').append(tableRow);
				}
			}
			var totalPortfolioValue = (parseInt($("#cashVal").text())+totalMarketPosition);
			var percentPortfolioBarWidth = (totalPortfolioValue*2)/1000;
			if(percentPortfolioBarWidth > 200) {
				percentPortfolioBarWidth = 200;
			}
			else if(percentPortfolioBarWidth < 0) {
				percentPortfolioBarWidth = 0;
			}

			$(".portfolio_inner_container").css("width",percentPortfolioBarWidth);
			$("#portVal").text(totalPortfolioValue);

	});

	$("#buyStocksLink").click(function() {
		$("#buyStocksLink").css("color","#8580F7");
	});

	
	function makeTableRows(tick,marketVal,bookVal,originalPrice,currentPrice,percentGain,color) {
		var row = "<tr><td style=\"color:"+color+";font-weight:bold\">"+tick+"</td>"+
							"<td>"+bookVal+"</td>"+
							"<td style=\"color:"+color+";font-weight:bold\">"+marketVal+"</td>"+
							"<td>"+originalPrice+"</td>"+
							"<td style=\"color:"+color+";font-weight:bold\">"+currentPrice+"</td>"+
							"<td style=\"color:"+color+";font-weight:bold\">"+percentGain+" %" +"</td></tr>";
		return row;
	}

});