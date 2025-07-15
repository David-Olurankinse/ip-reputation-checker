import requests

API_KEY = 'ba3280150c9f7f09a439eafe74ec30387f68aecafca8cc6bd2555931cd9c9fe49b16c0b4dcd00fd7'
BASE_URL = 'https://api.abuseipdb.com/api/v2/check'

def check_ip(ip_address):
    headers = {
        'Accept': 'application/json',
        'Key': API_KEY
    }
    params = {
        'ipAddress': ip_address,
        'maxAgeInDays': 90
    }
    response = requests.get(BASE_URL, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()['data']
        print(f"IP Address: {data['ipAddress']}")
        print(f"Abuse Confidence Score: {data['abuseConfidenceScore']}")
        print(f"Country: {data['countryCode']}")
        print(f"Usage Type: {data.get('usageType', 'N/A')}")
        print(f"ISP: {data.get('isp', 'N/A')}")
        print(f"Domain: {data.get('domain', 'N/A')}")
        print(f"Total Reports: {data['totalReports']}")
        print(f"Last Reported: {data.get('lastReportedAt', 'N/A')}")
    else:
        print(f"Error fetching data: {response.status_code}")

if __name__ == '__main__':
    ip = input("Enter IP address to check: ")
    check_ip(ip)
