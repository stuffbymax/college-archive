// universal.js

// Function to fetch weather data
const getWeatherData = async (latitude, longitude) => {
    const api_url = `https://api.open-meteo.com/v1/forecast?latitude=latitude&longitude=longitude&hourly=temperature_2m,relative_humidity_2m,dew_point_2m,precipitation_probability,precipitation,rain,pressure_msl,surface_pressure,cloud_cover,cloud_cover_low,cloud_cover_high,visibility,evapotranspiration,et0_fao_evapotranspiration,vapour_pressure_deficit&timezone=Europe%2FLondon`;
  
    try {
      const response = await fetch(api_url);
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      const data = await response.json();
      return data;
    } catch (error) {
      console.error("Error fetching weather data:", error);
      throw error; // Re-throw the error to be handled by the caller
    }
  };
  
  // Function to display weather data (adaptable to different environments)
  const displayWeatherData = (data, targetElement) => {
    if (!data || !data.hourly || !data.hourly.time) {
      console.error("Invalid API response:", data);
      targetElement.innerHTML = "<p>Error: Invalid weather data.</p>";
      return;
    }
  
    let htmlContent = `
      <p><span class="label">Latitude:</span> ${data.latitude}</p>
      <p><span class="label">Longitude:</span> ${data.longitude}</p>
      <p><span class="label">Elevation:</span> ${data.elevation}</p>
      <p><span class="label">Temperature Unit:</span> ${data.temperature_unit}</p>
      <p><span class="label">Wind Speed Unit:</span> ${data.windspeed_unit}</p>
      <p><span class="label">Precipitation Unit:</span> ${data.precipitation_unit}</p>
      <h2>Hourly Data</h2>
    `;
  
    for (let i = 0; i < data.hourly.time.length; i++) {
      htmlContent += `
        <div class="hourly-data">
          <p><span class="label">Time:</span> ${data.hourly.time[i]}</p>
          <p><span class="label">Temperature:</span> ${data.hourly.temperature_2m[i]} ${data.temperature_unit}</p>
          <p><span class="label">Relative Humidity:</span> ${data.hourly.relativehumidity_2m[i]}%</p>
          <p><span class="label">Precipitation Probability:</span> ${data.hourly.precipitation_probability[i]}%</p>
          <p><span class="label">Precipitation:</span> ${data.hourly.precipitation[i]} ${data.precipitation_unit}</p>
          <p><span class="label">Rain:</span> ${data.hourly.rain[i]} mm</p>
          <p><span class="label">Cloud Cover:</span> ${data.hourly.cloudcover[i]}%</p>
          <p><span class="label">Vapour Pressure Deficit:</span> ${data.hourly.vapour_pressure_deficit[i]} hPa</p>
          <p><span class="label">Evapotranspiration:</span> ${data.hourly.evapotranspiration[i]} mm</p>
        </div>
      `;
    }
  
    targetElement.innerHTML = htmlContent;
  };

  getWeatherData();
  
 