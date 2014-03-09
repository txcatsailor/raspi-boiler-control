%#template for editing a task
%#the template expects to receive a value for "no" as well a "old", the text of the selected ToDo item
<p>Edit the Schedule with ID = {{id_shed}}</p>
<form action="/edit/{{id_shed}}" method="POST">
<input type="text" name="id_shed" value="{{old[0]}}" >
<input type="text" name="day" value="{{old[1]}}" >
<input type="text" name="time" value="{{old[2]}}" >
<input type="text" name="state" value="{{old[3]}}" >
</select>
<br/>
<input type="submit" name="save" value="save">
</form>