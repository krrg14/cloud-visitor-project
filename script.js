async function getVisitorCount() {

    const response = await fetch("https://segata4k3h.execute-api.ap-south-1.amazonaws.com");

    const data = await response.json();

    document.getElementById("visitor-count").innerText = data.count;
}

getVisitorCount();
