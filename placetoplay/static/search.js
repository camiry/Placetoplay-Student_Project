$(document).ready(function()
{
	var groupStuff = 
	{
		groupName: "Example Group",
		groupAddress: "555 Anystreet USA"
	};
	var template = $('#result-template').html();
	var html = Mustache.render(template, groupStuff);
	for (var i=0; i < 5; i++)
	{
		$('#results').append(html);
		console.log('lol');
	}
});