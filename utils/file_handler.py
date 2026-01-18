def read_sales_data(filename):
    """
    Reads sales data from file handling encoding issues.

    Returns:
        list of raw transaction lines (strings), excluding header and empty lines.

    Requirements:
    - Use 'with' statement
    - Handle different encodings (try 'utf-8', 'latin-1', 'cp1252')
    - Handle FileNotFoundError with appropriate error message
    - Skip the header row
    - Remove empty lines
    """

    encodings_to_try = ["utf-8", "latin-1", "cp1252"]

    for enc in encodings_to_try:
        try:
            with open(filename, "r", encoding=enc) as f:
                lines = f.readlines()
            break  # Successfully read file, exit loop
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
            return []
        except UnicodeDecodeError:
            # Try next encoding
            continue
    else:
        # If all encodings fail, fallback with replacement characters
        with open(filename, "r", encoding="latin-1", errors="replace") as f:
            lines = f.readlines()

    # Remove header (first line) and strip empty lines
    data_lines = [line.strip() for line in lines[1:] if line.strip() != ""]

    return data_lines