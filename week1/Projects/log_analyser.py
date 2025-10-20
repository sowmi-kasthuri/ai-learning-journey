# Log Analyzer

## What it does:
# Analyzes log files, counts errors/warnings, shows patterns

## Features:
# Count total lines
# Count ERROR lines
# Count WARNING lines  
# Show sample errors
# Export summary

## Standard .txt file with simple error/warning messages:

## Functions:
# main() - Get filename, call analyzer
def main():
    file_name = "Log.txt"
    analyze_log (file_name)
   

# analyze_log(filename) - Read and process
def analyze_log(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
    stats = count_error(lines)
    display_summary(stats)

# count_errors(lines) - Count ERROR lines
def count_error(lines):
    line_count = len(lines)
    error_count = 0
    warning_count = 0
    for line in lines:
        line_lower = line.lower()
        if "error" in line_lower:
            error_count += 1
        if "warning" in line_lower:
            warning_count += 1
    return line_count, error_count, warning_count

# display_summary(data) - Print results
def display_summary(stats):
     line_count, error_count, warning_count = stats
     print(f"Total Lines = {line_count}")
     print(f"Total Errors = {error_count}")
     print(f"Total Warnings = {warning_count}")


main()