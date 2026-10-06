import re
from pathlib import Path
from typing import Dict, Any
import duckdb

#Patterns for type recognition(Mostly by time which is dumb)
WINDOWS_PATTERN = re.compile(r"\b\d{4}[\-./]\d{2}[\-./]\d{2}\b") # <- Here i check if the date in a YYYY-MM-DD format(As given in the test_data directory)
LINUX_PATTERN = re.compile(r"\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d+\s+\d{2}:\d{2}:\d{2}\b")
SSH_PATTERN = re.compile(r'sshd\[\d+\]') # <- Here i take ssh[xxxx] part and check if it's present in logs
APACHE_PATTERN = re.compile(r'\[(?:Mon|Tue|Wed|Thu|Fri|Sat|Sun)\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{2}\s+\d{2}:\d{2}:\d{2}\s+\d{4}]')

#Setting up REGEX(Regular Expressions) schemas for duckdb
REGEX_SCHEMAS = {
    "windows": r'^(\\d{4}-\\d{2}-\\d{2}\\s+\\d{2}:\\d{2}:\\d{2}),\\s+(\\w+)\\s+(\\w+)\\s+(.*)\$',
    
    "linux": r'^([A-Z][a-z]{2}\\s+\\d+\\s+\\d{2}:\\d{2}:\\d{2})\\s\(+(\S+)\\\)s+(\\w+)(?:\\[\\d+\\])?:\\s+(.*)\$',
    
    "ssh": r'^([A-Z][a-z]{2}\\s+\\d+\\s+\\d{2}:\\d{2}:\\d{2})\\s\(+(\S+)\\\)s+(sshd)\\[(\\d+)\\]:\\s+(.*)\$',
    
    "apache": r'^\\[((?:Mon\vert{}Tue\vert{}Wed\vert{}Thu\vert{}Fri\vert{}Sat\vert{}Sun)\\s+[A-Z][a-z]{2}\\s+\\d{2}\\s+\\d{2}:\\d{2}:\\d{2}\\s+\\d{4})\\]\\s+\\[(\\w+)\\]\\s+\\[([^\\]]+)\\]\\s+(.*)\$'
}

#Checking what type of log is given(Window, Linux, SSH or APACHE)
def detect_log_family(file_path: Path) -> str:
    with open(file_path, 'r', encoding="utf-8", errors='ignore') as f:
        lines = [f.readline() for _ in range(5)]
        sample = '\n'.join(lines)
        
    checks = [
        ("windows", WINDOWS_PATTERN), 
        ("linux", LINUX_PATTERN),
        ("ssh", SSH_PATTERN),
        ("apache", APACHE_PATTERN)
    ]
    
    for log_type, pattern in checks:
        if pattern.search(sample):
            return log_type
    
    raise ValueError("Unknown log file!")

#Analyzing with duckdb for best performance

def analyzer(file_path: Path) -> Dict[str, Any]:
    log_family = detect_log_family(file_path=file_path)
    regex_pattern = REGEX_SCHEMAS[log_family]
    
    db_con = duckdb.connect(database=':memory:')
    
    sql_safe_path = str(file_path.resolve()).replace('\\', '/')
    