const q = document.getElementById("search");

function dosearch() {
    if (q.value.length > 0) {
        fetch("/search/" + q.value)
        .then((response) => response.text())
        .then((results) => (document.getElementById("resTable").innerHTML = results));
    }
};