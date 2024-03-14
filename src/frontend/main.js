function sample() {
    var input = document.getElementById("input")
    fetch("http://127.0.0.1:8000/generate",  {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: input.innerHTML })
    })
    .then(response => response.json())
    .then(data => {
        var output = document.getElementById("output")
        output.innerText = data.result
    })
}
