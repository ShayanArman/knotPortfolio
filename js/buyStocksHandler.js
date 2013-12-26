$(document).ready(function() {
	var sharePrice = 0;
	var percent = ((($("#cashVal").text())/100000)*100)*2;
	$(".cash_inner_container").css("width",percent);

	/* Search stock price button was pressed! */
	$("#querystockbutton").click(function() {
		$('#querystockbutton').attr('disabled', 'disabled');

		var numberSharesInput = $("#quantitySharesInput").val();
		var quoteToSearch = $("#priceSearchInput").val().toUpperCase();
		if(quoteToSearch != "") {
			queryPrice(quoteToSearch);
			if(getInt(numberSharesInput) != 'wrong') {
				setTimeout(function(){
		        		setMirrorInput("$ " + (numberSharesInput*sharePrice).toFixed(2));
		        },1000);
			}
		}
	});

	/* Number of shares was updated, change the total price. */
    $('#quantitySharesInput').keyup(function(event) {
        var numberSharesDog = $('#quantitySharesInput').val();
        rightFormat = (getInt(numberSharesDog) != 'wrong');
        numberGreaterThanZero = (numberSharesDog > 0);
        goodSharePrice = (sharePrice != 0);

        if(goodSharePrice && rightFormat && numberGreaterThanZero) {
        	setMirrorInput("$ " + (numberSharesDog*sharePrice).toFixed(2));
        } 
        else if(!goodSharePrice && rightFormat && numberGreaterThanZero) {
        	var input = $("#priceSearchInput").val().toUpperCase();
        	if(input != ""){
        		enterStockSymbolAndUpdatePrice(input,numberSharesDog);
        	} else {
        		setMirrorInput("Enter A Stock Symbol");
        		setTimeout(function(){
        			var input = $("#priceSearchInput").val().toUpperCase();
        			enterStockSymbolAndUpdatePrice(input,numberSharesDog);
        		},4000);
        	}
        }
        else if(!rightFormat && numberSharesDog != "") {
        	setMirrorInput("Enter A Proper Number");
        }
        else if(numberSharesDog == 0) {
        	setMirrorInput("$ 0.00");	
        }
    });

	/* Buy stocks button was clicked. Check to see if the parameters are right. Then buy the stock.  */
	$("#buystocksbutton").click(function() {
		$('#buystocksbutton').attr('disabled', 'disabled');
		var ticker = $("#priceSearchInput").val().toUpperCase();
		var numberOfShares = $("#quantitySharesInput").val()
		if(getInt(numberOfShares) != 'wrong' && numberOfShares > 0) {
			$.getJSON("/render/"+ticker.toUpperCase()+"/"+numberOfShares).complete(function(data) {
				loadedValues = data.responseText;
				var response = String(loadedValues);
	
					if(response == 'Error') {
						setMirrorInput('Error, Please Try Again');
					} 
					else if(response == 'NotEnoughCash') {
						setMirrorInput('Not Enough Cash Available');
					}
					else {
						window.location.href = "/";
					}
					$('#buystocksbutton').removeAttr('disabled');
			});
		} else {
			setMirrorInput('Enter A Proper Number');
			$('#buystocksbutton').removeAttr('disabled');
		}
	
	});

	function enterStockSymbolAndUpdatePrice(input,numberSharesDog) {
    	if(input != "" && sharePrice == 0){
    		queryPrice(input);
    		setTimeout(function(){
    			if(sharePrice != 0) {
    				setMirrorInput("$ " + (numberSharesDog*sharePrice).toFixed(2));
    			} else {
    				setMirrorInput("Query A Proper Stock Symbol");		
    			}
    		},1500);
    	}
	}
	/*  Change the total cost input to represent the total cost or the warning terms  */
	function setMirrorInput(totalCost) {
		$('#mirrorInput').val(totalCost);
	}

	/* Hit the database to get the stock price. Update the price in the retrieved field. */
	function queryPrice(quoteToSearch) {
		$.getJSON("/getPrice/"+quoteToSearch).complete(function(data) {

			sharePrice = String(data.responseText);
			if(sharePrice == 'Error') {
				sharePrice = 0;
			} else {
				$("#retrievedStockHolder").show();
				$("#priceRetrieved").val("Price : $"+sharePrice);
				$("#priceSearchInput").val(quoteToSearch);
			}
			$('#querystockbutton').removeAttr('disabled');
		});
	}

	/* Check to see if the proper format was used for the number of shares. I.e not 3s, 3.34, -1.3*/
	function getInt(x) {
	    if (typeof x !== "number" && typeof x !== "string" || x === "") {
	        return 'wrong';
	    } else {
	        x = Number(x);
	        return x === Math.floor(x) ? x : 'wrong';
	    }
	}

});