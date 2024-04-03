import sys
import re

def print_help():
    print("Usage: python3 grep.py [-c] [-i] [-h] pattern filename")
    print("Options:")
    print("  -c    Print only the count of matches.")
    print("  -i    Ignore case when searching for the pattern.")
    print("  -h    Print this help message.")
    print("  pattern    The regular expression pattern to search for.")
    print("  filename   The name of the file to search in.")

def grep(pattern, filename, count=False, ignore_case=False):
    pattern_count = 0
    flags = re.IGNORECASE if ignore_case else 0
    with open(filename) as f:
        for line_num, line in enumerate(f, start=1):
            matches = re.findall(pattern, line, flags=flags)
            pattern_count += len(matches)
            if count:
                continue
            if matches:
                for match in matches:
                    start = line.lower().find(match.lower())  # Adjust for case insensitive search
                    end = start + len(match)
                    highlighted_line = (line[:start] +
                                        "\033[91m" +  # ANSI escape code for red color
                                        match +
                                        "\033[0m" +   # ANSI escape code to reset color
                                        line[end:])
                    print(f"Line {line_num}: {highlighted_line.strip()}")
    if count:
        print(f"The pattern '{pattern}' occurred {pattern_count} times in the file.")

if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "-h":
        print_help()
    elif len(sys.argv) >= 3:
        pattern = sys.argv[-2]
        filename = sys.argv[-1]
        count_flag = False
        ignore_case_flag = False
        if sys.argv[1] == "-c":
            count_flag = True
        elif sys.argv[1] == "-i":
            ignore_case_flag = True
        elif sys.argv[1] == "-ci" or sys.argv[1] == "-ic":
            count_flag = True
            ignore_case_flag = True
        grep(pattern, filename, count=count_flag, ignore_case=ignore_case_flag)
    else:
        print("Invalid usage. Run 'python3 grep.py -h' for help.")
