# Random User-Agent Curl Request Script

## Description
This Python script automates sending HTTP requests to a specified URL using `curl`. Each request is made with a randomly generated User-Agent string, simulating different devices and browsers. This approach helps enhance anonymity and reduces the risk of detection or blocking based on repeated requests.

## Features
- Automatically generates a random User-Agent for each request.
- Uses `curl` for making HTTP requests.
- Simple and easy to use.

## Requirements
- Python 3.x
- `requests` library (optional, for expanding functionality)

## Installation
```bash
# Clone the repository
git clone <repository_url>
cd <repository_name>
```

## Usage
```bash
python3 curl_with_different_ag.py <URL>
```
Example:
```bash
python3 curl_with_different_agent.py https://example.com
```

## How It Works
1. The script generates a random User-Agent string.
2. It executes a `curl` command with the `-A` option to set the User-Agent header.
3. Sends the HTTP request to the specified URL.

## Example Output
```
Making request to https://example.com with User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36
Response: <HTML Response or Status>
```

## Customization
- You can modify the User-Agent pool in the script to suit your needs.
- Add additional request headers or expand the script to support POST requests if needed.

## Contributing
Feel free to fork this repository and submit pull requests with improvements.

## License
This project is licensed under the MIT License.

## Disclaimer
This script is intended for educational purposes only. Use responsibly and ensure compliance with applicable laws and website terms of service.

