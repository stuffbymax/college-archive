/* nasa_api.js JavaScript to access the NASA Mars Photos API Author: martin Petik Version 0.01 licence: MIT */
alert("hello from javascript");
 
const output_div = document.getElementById("output");
const image_div = document.getElementById("photo");
let json_data; // Declare json_data in the global scope.
 
const myRequest = new Request(
"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=QFmdWdZ4CmEsuhbqkzuLi6WEBtjoGMraWtqJiYDa"
);
 
async function getData() {
  const response = await fetch(myRequest);
  json_data = await response.json(); 
  console.log(json_data);
 
  const elementCount = Object.keys(json_data['photos']).length;
  console.log(elementCount);
 
  let outputmessage = elementCount + 'id, sol, camera, img_src, earth_date, rover<br>';
  Object.keys(json_data).forEach(key => {
    
  });
  outputmessage += `Photo<br>`;

  output_div.innerHTML = outputmessage; // Set the initial message
 
  const image_url = json_data['photos'][0]['img_src'];
  outputmessage = elementCount + ' keys: id, sol, camera, img_src, earth_date, rover<br>';
  output_div.innerHTML = outputmessage
  image_div.innerHTML = '<img src="' + image_url + '" width="200" height="200">';
 
}
 
getData();