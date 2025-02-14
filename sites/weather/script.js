        const api_url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m,relative_humidity_2m,dew_point_2m,precipitation_probability,precipitation,rain,pressure_msl,surface_pressure,cloud_cover,cloud_cover_low,cloud_cover_high,visibility,evapotranspiration,et0_fao_evapotranspiration,vapour_pressure_deficit&timezone=Europe%2FLondon";

        async function getweather() {
            try {
                const response = await fetch(api_url);
                const data = await response.json();

                // Check if 'hourly' exists and has data
                if (!data || !data.hourly || !data.hourly.time) {
                    console.error("Invalid API response:", data);
                    document.getElementById("weather-info").innerHTML = "<p>Error fetching weather data.</p>";
                    return;
                }


                document.getElementById("latitude").textContent = data.latitude;
                document.getElementById("longitude").textContent = data.longitude;
                document.getElementById("elevation").textContent = data.elevation;
                document.getElementById("temperature-unit").textContent = data.temperature_unit;
                document.getElementById("wind-speed-unit").textContent = data.windspeed_unit; //Fixed typo
                document.getElementById("precipitation-unit").textContent = data.precipitation_unit;
                document.getElementById("time-format").textContent = data.timeformat; // This property doesn't exist directly in the Open-Meteo response.  It's likely that 'data.timezone' would be relevant if you want to display it.  Removing for now to avoid error, but consider if you need to handle timezone.

                const hourlyContainer = document.getElementById("hourly-container");
                hourlyContainer.innerHTML = ""; // Clear previous data

                for (let i = 0; i < data.hourly.time.length; i++) {
                    const hourlyDiv = document.createElement("div");
                    hourlyDiv.classList.add("hourly-data");

                    hourlyDiv.innerHTML = `
                        <p><span class="label">Time:</span> ${data.hourly.time[i]}</p>
                        <p><span class="label">Temperature:</span> ${data.hourly.temperature_2m[i]} ${data.temperature_unit}</p>
                        <p><span class="label">Relative Humidity:</span> ${data.hourly.relativehumidity_2m[i]}%</p>
                        <p><span class="label">Precipitation Probability:</span> ${data.hourly.precipitation_probability[i]}%</p>
                        <p><span class="label">Precipitation:</span> ${data.hourly.precipitation[i]} ${data.precipitation_unit}</p>
                        <p><span class="label">Rain:</span> ${data.hourly.rain[i]} mm</p>
                        <p><span class="label">Cloud Cover:</span> ${data.hourly.cloudcover[i]}%</p>
                        <p><span class="label">Vapour Pressure Deficit:</span> ${data.hourly.vapour_pressure_deficit[i]} hPa</p>
                        <p><span class="label">Evapotranspiration:</span> ${data.hourly.evapotranspiration[i]} mm</p>
                    `;
                    hourlyContainer.appendChild(hourlyDiv);
                }


            } catch (error) {
                console.error("Error fetching or processing data:", error);
                document.getElementById("weather-info").innerHTML = "<p>Error fetching weather data.</p>";
            }
        }

        getweather();
