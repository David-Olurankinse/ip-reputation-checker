# IP Reputation Checker

This Python script checks the reputation of any IP address using AbuseIPDB's free API. Useful for SOC analysts, blue teams, and cybersecurity students who want to quickly investigate suspicious IPs.

---

## Features

- Lookup IP reputation in real time
- Displays abuse confidence score, ISP, usage type, and more
- Simple CLI input for fast checks
- Powered by [AbuseIPDB](https://www.abuseipdb.com/)

---

## Setup

1. Clone the repo:

```bash
git clone https://github.com/yourusername/ip-reputation-checker.git
cd ip-reputation-checker
```

2. Install dependencies:
```bash
pip install requests
```

3. Replace YOUR_API_KEY_HERE in ip_checker.py with your own AbuseIPDB API key.

Usage 
```bash
python ip_checker.py
```

Enter an IP address when prompted. Example output:
```bash
--- IP Reputation Report ---
IP Address           : 203.0.113.88
Abuse Confidence     : 85%
Country              : US
ISP                  : Evil ISP Ltd.
Domain               : badhost.example.com
Usage Type           : Data Center/Web Hosting/Transit
Total Reports        : 47
Last Reported        : 2024-05-22T11:30:45Z
```

Make sure not to share your API key publicly. For production use, consider loading it from a .env file.


Author 
David Olurankinse
https://www.linkedin.com/in/david-o-98210122b/