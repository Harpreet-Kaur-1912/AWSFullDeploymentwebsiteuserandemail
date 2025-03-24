document.getElementById('userForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    await fetch('<API_GATEWAY_URL>', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, email })
    });
    alert('Submitted successfully!');
});