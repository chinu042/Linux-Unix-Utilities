# grep Utility

This repository contains a Python script `grep.py` which provides functionality similar to the Unix `grep` command. It allows users to search for a specified pattern within a file and perform various operations such as printing matching lines, counting matches, and ignoring case sensitivity.

## Usage

### Prerequisites
- Python 3.x installed on your system.

### Flags
- `-c`: Print only the count of matches.
- `-i`: Ignore case when searching for the pattern.
- `-h`: Print help message.

### Usage
```
python3 grep.py [-c] [-i] [-h] pattern filename
```

### Examples

1. Search for a pattern in a file:
    ```
    python3 grep.py "pattern" filename
    ```

2. Print only the count of matches:
    ```
    python3 grep.py -c "pattern" filename
    ```

3. Ignore case when searching for the pattern:
    ```
    python3 grep.py -i "pattern" filename
    ```

4. Print help message:
    ```
    python3 grep.py -h
    ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
