document.getElementById("encode").addEventListener("submit", function (event) {
    event.preventDefault();

    var formData = new FormData(this);

    // Use AJAX to send the form data to the server
    fetch("/encode", {
        method: "POST",
            body: formData
        })
        .then(response => response.text())
        .then(data => {
        // Display the response on the page
        document.getElementById("response").innerHTML = "Encoded: " + data;
    })
    .catch(error => {
    console.error("Error:", error);
    });
});

