testing = True
dampener_engaged = True

if testing:
    f = open("input/testinput.txt", "r")
else:
    f = open("input/input.txt", "r")

safe_reports = 0
min_threshold = 1
max_threshold = 3
dampener_used = False

def determine_if_increasing(report):
    if int(report[0]) > int(report[1]):
        return False
    else:
        return True

def check_levels(level_1, level_2):
    if min_threshold <= level_1 - level_2 <= max_threshold:
        return 1
    return 0

def check_report(report):
    report_result = [0,0]

    if determine_if_increasing(report):
        # Report is increasing
        i = 0
        report_checks = 0
        print("checking increasing", report)
        while i + 1 < len(report):
            valid_levels = check_levels(int(report[i + 1]), int(report[i]))
            if valid_levels == 1:
                report_checks += 1
            else:
                report_result[1] = i

    else:
        # Report is decreasing

for line in f:
    report = line.split(" ")
    if determine_if_increasing(report):
        # Is Increasing
        i = 0
        report_checks = 0
        dampener_used = False
        dampener_candidate = -1
        print("checking increasing", report)
        while i+1 < len(report):
            valid_report = check_levels(int(report[i + 1]), int(report[i]))
            if valid_report == 0:
                dampener_candidate = i
            report_checks += valid_report
            i += 1
        if report_checks == len(report)-1:
            safe_reports += 1

    else:
        i = 0
        report_checks = 0
        dampener_used = False
        print("checking decreasing", report)
        while i + 1 < len(report):
            if min_threshold <= (int(report[i]) - int(report[i + 1])) <= max_threshold:
                print("valid", int(report[i + 1]), int(report[i]))
                report_checks += 1
            else:
                if dampener_engaged and not dampener_used:
                    report.remove(report[i+1])
                    dampener_used = True
            i += 1
        if report_checks == len(report)-1:
            safe_reports += 1

print(safe_reports)
