from fastapi import FastAPI
import psutil

app = FastAPI()
request_count = 0

@app.get("/")
def read_root():
    return {"message": "DevOps Monitoring Platform"}

@app.get("/health")
def health_check():
    global request_count
    request_count += 1
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    if disk.percent>90 or ram.percent>90 or cpu>90: 
        status = "warning"
        message = "Application is not running smoothly"
    else: 
        status = "healthy"
        message = "Application is running smoothly"

    return { 
    "cpu_usage": cpu , 
    "ram_usage": ram.percent,
    "disk_usage": disk.percent,
    "request_count": request_count,
    "status": status,
    "message": message}

@app.get("/status")
def status_check():
    return {"status":"operational"}