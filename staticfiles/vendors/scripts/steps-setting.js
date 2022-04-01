$(".tab-wizard").steps({
	headerTag: "h5",
	bodyTag: "section",
	transitionEffect: "fade",
	titleTemplate: '<span class="step">#index#</span> #title#',
	labels: {
		finish: "Submit"
	},
	onStepChanged: function (event, currentIndex, priorIndex) {
		console.log('wiz1_changed')
		$('.steps .current').prevAll().addClass('disabled');
	},
	onFinished: function (event, currentIndex) {
		console.log('wiz1')
		$('#success-modal').modal('show');
	}
});

$(".tab-wizard2").steps({
	headerTag: "h5",
	bodyTag: "section",
	transitionEffect: "fade",
	titleTemplate: '<span class="step">#index#</span> <span class="info">#title#</span>',
	labels: {
		finish: "Submit",
		next: "Next",
		previous: "Previous",
	},
	onStepChanged: function(event, currentIndex, priorIndex) {
		console.log('wiz2_changed')
		$('.steps .current').prevAll().addClass('disabled');
	},
	onFinished: function(event, currentIndex) {
		profile_type = $("input[type='radio'][name='profile_type']:checked").val()
		full_name = $('#full_name').val()
		email = $('#email').val()
		gender = $("input[type='radio'][name='gender']:checked").val()
		username = $('#username').val()
		password = $('#password').val()
		country = $('#country').val()
		state = $('#state').val()
		city = $('#city').val()
		data = {}
		data['profile_type'] = profile_type
		data['full_name'] = full_name
		data['email'] = email
		data['gender'] = gender
		data['username'] = username
		data['password'] = password
		data['country'] = country
		data['state'] = state
		data['city'] = city
		$.ajax({
			type: 'POST',                 
			url: '/api/register/',
			dataType:'json',
			data: data,
			success: function (data, abc) {
				var error = document.getElementsByClassName("error")[0];
				if (data['status'] == 200 || data['status'] == '200')
				{
					$('#success-modal-btn').trigger('click');
				} else {
					error.innerText = data['message']
				}
			},
			error: function(XMLHttpRequest, textStatus, errorThrown) { 
				alert("Registration failed");
			}
		});

	}
});