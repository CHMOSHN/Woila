from parser import detect_log_family
import csv

#Function for sterilization of standart .log file into a nice CSV one four future analysis
def sterilization(file_path: str) -> None:
    
    log_family = detect_log_family(file_path=file_path)
    with open(file_path, 'r', encoding='utf-8') as f:
        match log_family:
            case "windows":
                with open('win.csv', 'w', encoding="utf-8-sig", newline='') as out:
                    writer = csv.writer(out)
                    writer.writerow(("datetime ", "log_type", "component", "message"))
                    
                    for line in f:
                        datetime, other = line.split(',', 1)
                        other = other.strip()
                        log_type, component, message = other.split(None, 2)
                        writer.writerow([datetime, log_type, component, message])
                        
            case "linux":
                with open("lin.csv", 'w', encoding='utf-8-sig', newline='') as out:
                    writer = csv.writer(out)
                    writer.writerow(("datetime", "user", "component", "message"))
                    
                    for line in f:
                        splitted = line.split(' ')
                        datetime, user, component, message = ' '.join(splitted[:3]), splitted[3], splitted[4], ' '.join(splitted[5:])
                        writer.writerow([datetime, user, component, message])

            case "apache":
                with open('apa.csv', 'w', encoding="utf-8-sig", newline='') as out:
                    ...