async function get_visitors() {
    try {
        let response = await fetch('https://1l3i8r39t1.execute-api.us-east-1.amazonaws.com/Prod/visitor-count');

        let data = await response.json(); // Parse JSON

        console.log("Raw API Response:", data); // Debugging log

        // ✅ Check and display visitor count properly
        if (data["visitor-count"] !== undefined) {
            document.getElementById("visitors").innerHTML = data["visitor-count"];
        } else {
            console.error("Error: `visitor-count` missing from response.");
            document.getElementById("visitors").innerHTML = "Error fetching count";
        }
    } catch (err) {
        console.error("Error fetching visitor count:", err);
        document.getElementById("visitors").innerHTML = "Error";
    }
}

// Call function
get_visitors();