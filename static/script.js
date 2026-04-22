function updateWeather() {
    const output = document.getElementById("output");
    const now = new Date();
    let time = now.toLocaleTimeString();

    let emoji = "";
    let advice = "";
    let desc = window.desc.toLowerCase();

    if (desc.includes("rain")) {
        emoji = "🌧️";
        advice = "Take umbrella ☂️";
    } else if (desc.includes("hot")) {
        emoji = "🔥";
        advice = "Drink water 💧";
    } else if (desc.includes("cool")) {
        emoji = "❄️";
        advice = "Wear jacket 🧥";
    } else {
        emoji = "☀️";
        advice = "Enjoy weather 😎";
    }

    output.innerHTML = `
    ${emoji} Time = ${time} |
    🌡️ Temp = ${window.temp}°C |
    💧 Humidity = ${window.humidity}% |
    📍 ${window.city} |
    ${window.desc} → ${advice}
    `;
}

setInterval(updateWeather, 1000);
updateWeather();
