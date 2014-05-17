<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Schedule</title>

    <!-- Bootstrap -->
    <link href="css/bootstrap.min.css" rel="stylesheet">

    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
      <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>
  <body>
    <div class="container">
    <h1>Boiler Schedule</h1>
    
    <h3>Template</h3>
    	<form class="form-inline" role="form" action="/getschedule" method="POST">
			<div class="form-group">
			    <select class="form-control" name="tmpl">
			        %for item in tmpl: 
			        <option value="{{item}}">{{item}}
			        %end
			    </select>
			</div>
			<button type="submit" name="select" value="select" class="btn btn-default">Select</button>
		</form>
		<div class="panel panel-default">	
  			<div class="panel-heading">Schedule</div>
			  <table class="table">
			    %for row in rows:
			      %id_shed, day, time, state, template_name = row
			    <tr>
			    %for col in row:
			    <td>{{col}}</td>
			    %end
			    <td><a href="/edit/{{id_shed}}"> Edit</a></td>
			    <td><a href="/getschedule?delete=true&id_shed={{id_shed}}"> Delete</a></td>
			    </tr>
			    %end
			  </table>
			</div>
			<div class="btn-group">
				<form method="post" action="/newschedule">
					<button type="submit" class="btn btn-default">New</button>
		 		</form>
		 		<form method="post" action="/newtemplate">
					<button type="submit" class="btn btn-default">New Template</button>
		 		</form>
		 		<form method="post" action="/main">
					<button type="submit" class="btn btn-default">Back</button>
		 		</form>
			</div>
		</div>
	</div>
    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="js/bootstrap.min.js"></script>
  </body>
</html>