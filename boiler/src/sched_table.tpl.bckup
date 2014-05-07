%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
<p><h3>Boiler Schedule</h3></p>
<table border="1">
%for row in rows:
  %id_shed, day, time, state = row
  <tr>
  %for col in row:
    <td>{{col}}</td>
  %end
  <td><a href="/edit/{{id_shed}}"> Edit</a></td>
  </tr>
%end
</table>
<form method="post" action="/newschedule">
	<button type="submit">New</button>
</form>		