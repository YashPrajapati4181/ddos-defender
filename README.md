# DDoS Defender 🔒

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-green)
![Redis](https://img.shields.io/badge/Redis-7.0%2B-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

A cybersecurity tool to detect and mitigate DDoS/DoS attacks in real-time using Flask and Redis. Perfect for securing web applications against malicious traffic spikes.

![Setup_demo](https://github.com/user-attachments/assets/f9483777-0420-4ef6-bda3-cd9e9c67aba7)

## Features ✨

- 🛡️ **Real-Time Rate Limiting** - Track requests per IP using Redis
- 🔒 **IP Blocking** - Persist blocked IPs in SQLite database
- 🌍 **Geolocation Tracking** - Map attackers with ipinfo.io integration
- 📊 **JSON Logging** - Structured logs for attack forensics
- 🐳 **Docker Support** - Easy deployment with containerization

## Installation 🚀

### Prerequisites
- Python 3.9+
- Redis server
- Docker (optional)

```bash
# Clone the repository
git clone https://github.com/YashPrajapati4181/ddos-defender.git
cd ddos-defender

# Install dependencies
pip install -r requirements.txt

# Start Redis using Docker
docker run -d -p 6379:6379 --name redis-ddos redis
```

## Configuration ⚙️

Create `.env` file:
```env
IPINFO_API_KEY=your_ipinfo_key
REDIS_HOST=localhost
REQUEST_LIMIT=100  # Requests per minute
```

## Usage 💻

```bash
# Restart Redis using Docker
docker start redis-ddos 
# Start the Flask application
flask --app app/routes.py run --port=5000
```

### Simulate Attack locally curl
```bash
# Trigger rate limiting (run in separate terminal)
for i in {1..150}; do curl http://localhost:5000; done
```

### Check Blocked IPs
```bash
curl http://localhost:5000/blocked-ips
```

## Project Structure 📁
```
ddos-defender/
├── app/
│   ├── routes.py          # Flask endpoints
│   ├── rate_limiter.py    # Redis-based rate limiting
│   ├── ip_blocker.py      # IP blocking logic
│   └── utils.py           # Geolocation & logging
├── config.py              # Configuration loader
├── requirements.txt       # Dependencies
└── docker-compose.yml     # Container orchestration
```

## Contributing 🤝

1. Fork the repository
2. Create your feature branch:
```bash
git checkout -b feature/amazing-feature
```
3. Commit changes:
```bash
git commit -m 'Add some amazing feature'
```
4. Push to the branch:
```bash
git push origin feature/amazing-feature
```
5. Open a Pull Request

Please adhere to [Python PEP8](https://www.python.org/dev/peps/pep-0008/) standards.

## License 📄

Distributed under the MIT License. See `LICENSE` for more information.

---

**Made with ❤️ by Yash Prajapati And some help of DeepSeek**  
[![GitHub](https://img.shields.io/badge/GitHub-Profile-blue?style=for-the-badge&logo=github)](https://github.com/YashPrajapati4181)

