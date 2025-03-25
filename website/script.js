document.getElementById('userForm').addEventListener('submit', function(event) {
    event.preventDefault();

    let name = document.getElementById('name').value;
    let email = document.getElementById('email').value;
    fetch('https://6xxa5y0fzf.execute-api.us-east-1.amazonaws.com/dev', {  // Use your actual API Gateway URL here
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ name, email })
    })
    .then(response => response.json())
    .then(data => alert('Registration Successful'))
    .catch(error => console.error('Error:', error));
});
