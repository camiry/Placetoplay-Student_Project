$(document).ready(function()
{
	var fakeGame1 = []
	var fakeGame2 = []

	for(var i=0; i < 5; i++)
	{
		fakeGame1.push(Faker.Lorem.words());
		fakeGame2.push(Faker.Lorem.words());
		$('#popList').append('<li>' + fakeGame1[i] + '</li><br>');
		$('#newList').append('<li>' + fakeGame2[i] + '</li><br>');
	}
});