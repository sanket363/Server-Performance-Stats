# Server Performance Statistics Tool

A web-based utility for monitoring and analyzing server performance metrics in real-time. This tool provides a clean, modern interface to track CPU, memory, and disk usage statistics of your server.

## 🚀 Features

- **Real-time Monitoring**

  - Auto-refreshing dashboard every 5 seconds
  - Clean and modern web interface
  - JSON API endpoint for programmatic access

- **CPU Monitoring**

  - Total CPU usage percentage
  - Number of CPU cores

- **Memory Analysis**

  - Total memory usage statistics
  - Used and total memory in GB
  - Memory usage percentage

- **Disk Space Tracking**
  - Total disk usage metrics
  - Used and total disk space in GB
  - Disk usage percentage

## 📋 Prerequisites

- Python 3.6 or higher
- pip (Python package manager)

## 🛠️ Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/server-performance-stats.git
cd server-performance-stats
```

2. Create a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## 🚀 Usage

1. Start the server:

```bash
python main.py
```

2. Access the dashboard:

   - Open your web browser and navigate to `http://localhost:5000`
   - The dashboard will automatically refresh every 5 seconds

3. Access the JSON API:
   - Endpoint: `http://localhost:5000/stats`
   - Returns real-time performance metrics in JSON format

## 📊 API Response Format

```json
{
  "cpu": {
    "percent": 25.5,
    "cores": 4
  },
  "memory": {
    "percent": 65.2,
    "used_gb": 8.5,
    "total_gb": 16.0
  },
  "disk": {
    "percent": 72.1,
    "used_gb": 256.3,
    "total_gb": 512.0
  },
  "timestamp": "2024-03-14 12:34:56"
}
```

## 🔧 Dependencies

- Flask 2.0.1 - Web framework
- psutil 5.8.0 - System and process utilities

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.
