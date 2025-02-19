import sys
import requests
import random

def get_user_agents(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def make_request(url, user_agents):
    headers = {'User-Agent': random.choice(user_agents)}
    response = requests.get(url, headers=headers)
    return response

def main():
    if len(sys.argv) != 2:
        print("\033[91mError: Missing URL argument.\033[0m")
        print("Usage: python curl_with_different_agent.py <URL> \n")
        sys.exit(1)

    url = sys.argv[1]
    user_agents = get_user_agents('UserAgentList.txt')

    while True:
        response = make_request(url, user_agents)
        print(f"Status Code: {response.status_code}")
        if response.status_code != 403:
            print(response.text)
            break
        else:
            print("403 Forbidden - Changing User Agent")

if __name__ == "__main__":
    main()