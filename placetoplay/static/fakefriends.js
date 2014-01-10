$(document).ready(function()
{
	
	var randomFname = []
	var randomLname = []

	for (var i=0; i < 5; i++)
	{
		randomFname.push(Faker.Name.firstName());
		randomLname.push(Faker.Name.lastName());
		$('#fList').append('<li class=f'+i+'><img src="/static/friend.jpg" style="width: 50px; height: 50px; display-inline;">' + randomFname[i] + ' ' + randomLname[i] + '</li><br>');
	}
	
});