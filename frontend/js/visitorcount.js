async function get_visitors() {
    try {
        let response = await fetch('https://1l3i8r39t1.execute-api.us-east-1.amazonaws.com/Prod/visitor-count', {
            method: 'GET',
        });

        let data = await response.json();

        console.log("Raw API Response:", data); // Debugging line

        // Parse the "body" field which is a JSON string
        let bodyData = JSON.parse(data.body);

        console.log("Parsed Body Data:", bodyData); // Debugging line

        // Extract and display visitor count
        document.getElementById("visitors").innerHTML = bodyData["visitor-count"] || "Error";

        return bodyData;
    } catch (err) {
        console.error("Error fetching visitor count:", err);
    }
}

// Call function
get_visitors();