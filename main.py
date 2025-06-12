import psutil
from flask import Flask, jsonify
import time

app = Flask(__name__)

@app.route('/stats')
def get_stats():
    # CPU stats
    cpu_percent = psutil.cpu_percent(interval=1)
    cpu_count = psutil.cpu_count()
    
    # Memory stats
    memory = psutil.virtual_memory()
    memory_percent = memory.percent
    memory_used = memory.used / (1024 * 1024 * 1024)  # Convert to GB
    memory_total = memory.total / (1024 * 1024 * 1024)  # Convert to GB
    
    # Disk stats
    disk = psutil.disk_usage('/')
    disk_percent = disk.percent
    disk_used = disk.used / (1024 * 1024 * 1024)  # Convert to GB
    disk_total = disk.total / (1024 * 1024 * 1024)  # Convert to GB
    
    stats = {
        'cpu': {
            'percent': cpu_percent,
            'cores': cpu_count
        },
        'memory': {
            'percent': memory_percent,
            'used_gb': round(memory_used, 2),
            'total_gb': round(memory_total, 2)
        },
        'disk': {
            'percent': disk_percent,
            'used_gb': round(disk_used, 2),
            'total_gb': round(disk_total, 2)
        },
        'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
    }
    
    return jsonify(stats)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Server Performance Stats</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            .stats-container { max-width: 800px; margin: 0 auto; }
            .stat-box { 
                border: 1px solid #ddd;
                padding: 15px;
                margin: 10px 0;
                border-radius: 5px;
            }
            .stat-title { font-weight: bold; margin-bottom: 10px; }
            .stat-value { color: #2196F3; }
            .timestamp { color: #666; font-size: 0.9em; }
        </style>
    </head>
    <body>
        <div class="stats-container">
            <h1>Server Performance Stats</h1>
            <div id="stats"></div>
        </div>
        <script>
            function updateStats() {
                fetch('/stats')
                    .then(response => response.json())
                    .then(data => {
                        const statsHtml = `
                            <div class="stat-box">
                                <div class="stat-title">CPU Usage</div>
                                <div class="stat-value">${data.cpu.percent}% (${data.cpu.cores} cores)</div>
                            </div>
                            <div class="stat-box">
                                <div class="stat-title">Memory Usage</div>
                                <div class="stat-value">${data.memory.percent}% (${data.memory.used_gb}GB / ${data.memory.total_gb}GB)</div>
                            </div>
                            <div class="stat-box">
                                <div class="stat-title">Disk Usage</div>
                                <div class="stat-value">${data.disk.percent}% (${data.disk.used_gb}GB / ${data.disk.total_gb}GB)</div>
                            </div>
                            <div class="timestamp">Last updated: ${data.timestamp}</div>
                        `;
                        document.getElementById('stats').innerHTML = statsHtml;
                    });
            }
            
            // Update stats immediately and then every 5 seconds
            updateStats();
            setInterval(updateStats, 5000);
        </script>
    </body>
    </html>
    '''





