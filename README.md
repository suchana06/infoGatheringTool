<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
</head>
<body>
  <h1>IP Information Fetcher</h1>
  
  <p>This script fetches and displays various information about a given URL. It makes use of the <code>requests</code> and <code>socket</code> libraries to get the HTTP headers, IP address, and geographic information of the given URL.</p>

  <h2>Prerequisites</h2>
  <p>Make sure you have Python 3 installed on your system along with the <code>requests</code> library. You can install <code>requests</code> using pip if you haven't already:</p>
  
  <pre><code>pip install requests</code></pre>

  <h2>Usage</h2>
  <p>Run the script from the command line, passing the URL as an argument:</p>
  
  <pre><code>python script.py &lt;url&gt;</code></pre>
  
  <p>For example:</p>
  
  <pre><code>python script.py example.com</code></pre>

  <h2>Description</h2>
  <p>The script performs the following steps:</p>
  <ol>
    <li>Checks if a URL is provided as a command line argument. If not, it prints the usage information and exits.</li>
    <li>Prints the command line arguments.</li>
    <li>Sends a GET request to <code>http://google.com</code> and prints the response headers.</li>
    <li>Retrieves the IP address of the given URL using <code>socket.gethostbyname</code>.</li>
    <li>Sends a GET request to <code>https://ipinfo.io/&lt;IP&gt;/json</code> to get geographical information about the IP address.</li>
    <li>Parses the JSON response and prints the location and region of the IP address.</li>
  </ol>

  <h2>Example Output</h2>
  <pre><code>['script.py', 'example.com']</code></pre>
  
  <pre><code>{'Date': 'Mon, 20 May 2024 12:00:00 GMT', 'Content-Type': 'text/html; charset=ISO-8859-1', ...}</code></pre>

  <p>the ip of example.com is 93.184.216.34</p>

  <pre><code>{'ip': '93.184.216.34', 'city': 'Los Angeles', 'region': 'California', 'country': 'US', 'loc': '34.0522,-118.2437', ...}</code></pre>

  <p>location is: 34.0522,-118.2437<br>region is: California</p>

  <h2>Notes</h2>
  <ul>
    <li>Replace <code>example.com</code> with the URL you want to query.</li>
    <li>Ensure you handle possible exceptions (e.g., network issues, invalid URLs) in a production environment.</li>
  </ul>
</body>
</html>
