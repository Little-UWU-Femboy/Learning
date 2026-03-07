import csv
import hashlib
import re

inputFile = "tps757.csv"
deviceTypesFile = "deviceTypes.txt"
brandNamesFile = "brandNames.txt"
errorLogFile = "errors.log"

serialPattern = re.compile(r"^SN-[0-9a-f]{64}$", re.IGNORECASE)

devices = set()
brands = set()
seen = set()

processedLines = 0
errorsCount = 0

with (
    open(errorLogFile, "w", encoding="utf-8") as errorLog,
    open(inputFile, newline="", encoding="utf-8") as csvFile,
):
    reader = csv.reader(csvFile)

    for lineNum, row in enumerate(reader, start=0):
        processedLines += 1
        lineErrors = []

        if len(row) != 3:
            lineErrors.append(f"Incorrect number of columns ({len(row)})")
            errorsCount += 1

            if len(row) < 3:
                row += [""] * (3 - len(row))
            else:
                row = row[:3]

        deviceType, brand, serial = [col.strip() for col in row]

        if deviceType:
            devices.add(deviceType)

        if brand:
            brands.add(brand)

        if not deviceType:
            lineErrors.append("Missing device type")
            errorsCount += 1

        if not brand:
            lineErrors.append("Missing brand")
            errorsCount += 1

        if not serial:
            lineErrors.append("Missing serial number")
            errorsCount += 1

        if serial and not serialPattern.match(serial):
            lineErrors.append(f"Invalid serial number '{serial}'")
            errorsCount += 1

        record = f"{deviceType}|{brand}|{serial}"
        recordHash = hashlib.sha256(record.encode()).hexdigest()

        if recordHash in seen:
            lineErrors.append(f"Duplicate record '{deviceType}, {brand}, {serial}'")
            errorsCount += 1
        else:
            seen.add(recordHash)

        if lineErrors:
            errorLog.write(f"Line {lineNum}: {', '.join(lineErrors)}\n")

with open(deviceTypesFile, "w", encoding="utf-8") as f:
    for device in sorted(devices):
        f.write(device + "\n")

with open(brandNamesFile, "w", encoding="utf-8") as f:
    for brand in sorted(brands):
        f.write(brand + "\n")
