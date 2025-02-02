import ipinfo
import logging
from pythonjsonlogger import jsonlogger
from config import Config

def setup_logger():
    logger = logging.getLogger()
    handler = logging.StreamHandler()
    formatter = jsonlogger.JsonFormatter()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

def get_ip_details(ip: str) -> dict:
    try:
        handler = ipinfo.getHandler(Config.IPINFO_API_KEY)
        details = handler.getDetails(ip)
        
        return {
            "ip": ip,
            "hostname": details.hostname if hasattr(details, 'hostname') else "N/A",
            "city": details.city if hasattr(details, 'city') else "N/A",
            "country": details.country_name if hasattr(details, 'country_name') else "N/A",
            "org": details.org if hasattr(details, 'org') else "N/A",
            "latitude": details.latitude if hasattr(details, 'latitude') else "0.0",
            "longitude": details.longitude if hasattr(details, 'longitude') else "0.0"
        }
    except Exception as e:
        return {
            "ip": ip,
            "error": f"Failed to fetch details: {str(e)}"
        }
