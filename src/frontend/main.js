function sample() {

    alert("sending data")
    var textarea = document.getElementById("prompt")

    var response = fetch("http://127.0.0.1:8000/test",  {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: text })
    })
        .then(res => res.json())
        .then(data => alert(data))
    alert(response)
}
