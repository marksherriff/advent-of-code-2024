testing = False
dampener_engaged = True
safe_reports = 0
min_threshold = 1
max_threshold = 3
dampener_used = False
dampener_checked = 0

def determine_if_increasing(report):
    return int(report[0]) < int(report[1])

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
        #print("checking increasing", report)
        while i + 1 < len(report):
            valid_levels = check_levels(int(report[i + 1]), int(report[i]))
            if valid_levels == 1:
                report_checks += 1
            else:
                report_result[1] = i
            i += 1
        if report_checks == len(report)-1:
            report_result[0] = 1

    else:
        # Report is decreasing
        i = 0
        report_checks = 0
        #print("checking decreasing", report)
        while i + 1 < len(report):
            valid_levels = check_levels(int(report[i]), int(report[i + 1]))
            if valid_levels == 1:
                report_checks += 1
            else:
                report_result[1] = i
            i += 1
        if report_checks == len(report) - 1:
            report_result[0] = 1

    return report_result


### MAIN
if testing:
    f = open("input/testinput.txt", "r")
else:
    f = open("input/input.txt", "r")

for line in f:
    report = line.split(" ")
    report_status = check_report(report)
    if report_status[0] == 1:
        safe_reports += 1
    elif dampener_engaged:
        dampener_checked += 1
        print("Dampener engaged on ",report, "at position", report_status[1])
        left_report = report.copy()
        right_report = report.copy()

        left_report.pop(report_status[1])
        right_report.pop(report_status[1]+1)

        print("    LEFT", left_report)
        print("    RIGHT", right_report)
        left_status = check_report(left_report)
        right_status = check_report(right_report)
        if left_status[0] == 1 or right_status[0] == 1:
            safe_reports += 1
            print("    Dampener Worked!")
        else:
            print("    Dampener Failed!")


print(safe_reports)
print(dampener_checked)