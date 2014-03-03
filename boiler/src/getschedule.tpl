<html>
	<head>
		<title>Boiler Control</title>
	</head>
	<body>
		<h1>Schedule</h1>
		<form method="post" action="/setschedule">
			<input type="checkbox" name="monday" value="Monday">Monday<br>
			<input type="checkbox" name="tuesday" value="Tuesday">Tuesday<br>
			<input type="checkbox" name="wednesday" value="Wednesday">Wednesday<br>
			<input type="checkbox" name="thursday" value="Thursday">Thursday<br>
			<input type="checkbox" name="friday" value="Friday">Friday<br>
			<input type="checkbox" name="saturday" value="Saturday">Saturday<br>
			<input type="checkbox" name="sunday" value="Sunday">Sunday<br>
			<button type="submit">Get Schedule</button>
		</form>		
	</body>
</html>