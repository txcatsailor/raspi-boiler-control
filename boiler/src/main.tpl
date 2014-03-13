<html>
	<head>
		<title>Boiler Control</title>
	</head>
	<body>
		<h1>Main</h1>
		<form method="post" action="/newuser">
			<button type="submit">New User</button>
		</form>
		<br>
		<form method="post" action="/getschedule">
			<button type="submit">Set Schedule</button>
		</form>		
		<form method="post" action="/main">
			<input type="submit" name="override" value="override">
		</form>	
	</body>
</html>