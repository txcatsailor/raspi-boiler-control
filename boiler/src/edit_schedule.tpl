<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Boiler Control</title>

    <!-- Bootstrap -->
    <link href="../css/bootstrap.min.css" rel="stylesheet">

    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
      <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>
  <body>
	<div class="container">
		<h1>Edit Schedule</h1>
        <form class="form-inline" role="form" action="/edit/{{id_shed}}" method="POST">	
			<div class="form-group">
        		<input type="text" name="id_shed" class="form-control" disabled value="{{old[0]}}" >
        		<input type="hidden" name="id_shed" class="form-control" value="{{old[0]}}" >
        	</div>
			<div class="form-group">        			
        		<input type="text" name="day" class="form-control" disabled value="{{old[1]}}" >
        		<input type="hidden" name="day" class="form-control" value="{{old[1]}}" >
        	</div>
        	<div class="form-group">
        		<input type="time" name="time" class="form-control" value="{{old[2]}}" >
	        </div>
	        <div class="form-group">
	        	<input type="text" name="state" class="form-control" value="{{old[3]}}" >
    	    </div>
    	    <button type="submit" name="save" value="save" class="btn btn-default">Save</button>
    	    	
      		</form>
      	</div>
	 </div>
	<!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="../js/bootstrap.min.js"></script>
  </body>
</html>
