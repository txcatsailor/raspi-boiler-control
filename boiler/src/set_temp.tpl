<!DOCTYPE html>
<html>
	<head>
	    <meta charset="utf-8">
	    <meta http-equiv="X-UA-Compatible" content="IE=edge">
	    <meta name="viewport" content="width=device-width, initial-scale=1">
	    <title>Set Temperature</title>
	
	    <link rel="shortcut icon" href="libraries/favicon.ico">
		<link href="css/bootstrap.min.css" rel="stylesheet">
	
	    <script src="libraries/jquery-1.9.0.min.js"></script>
	    <script src="bootstrap/js/bootstrap.min.js"></script>
	    <script src="libraries/prettify/prettify.js"></script>
	    <script src="bootstrap-touchspin/bootstrap.touchspin.js"></script>
	</head>
	
	<body>
		<div class="container">
		    <h1>Set Target Temperature</h1>
	
			    <div class="form-group">
			        <form class="form-inline" action="/settemp" method="POST"> 
				        <input
				            id="temp"
				            type="text"
				            %for i in curr_temp:
				            	%temp=i
				            value={{temp}}
				            %end
				            name="temp"
				            data-bts-min="0"
				            data-bts-max="100"
				            data-bts-init-val=""
				            data-bts-step="1"
				            data-bts-decimal="0"
				            data-bts-step-interval="100"
				            data-bts-force-step-divisibility="round"
				            data-bts-step-interval-delay="500"
				            data-bts-prefix=""
				            data-bts-postfix=""
				            data-bts-prefix-extra-class=""
				            data-bts-postfix-extra-class=""
				            data-bts-booster="true"
				            data-bts-boostat="10"
				            data-bts-max-boosted-step="false"
				            data-bts-mousewheel="true"
				            data-bts-button-down-class="btn btn-default"
				            data-bts-button-up-class="btn btn-default"
				            class="form-control"
				            >
				
					<script>
						$("input[name='temp']").TouchSpin({
					            });
					</script>
					<br />
					<input type="submit" class="btn btn-default" name="save" value="Save">
					</form>
					<form action="/main">
		    			<input type="submit" class ="btn btn-default" value="Back">
					</form>
				</div>
		</div>
		<!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
	    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
	    <!-- Include all compiled plugins (below), or include individual files as needed -->
	    <script src="js/bootstrap.min.js"></script>
	</body>
</html>