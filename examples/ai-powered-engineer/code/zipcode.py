import re

def extract_zip_codes(text):
    """
    Extract all US zip codes in 5-digit format from the input text.
    
    Args:
        text (str): The input text to search for zip codes
        
    Returns:
        list: A list of all 5-digit zip codes found in the text
    """
    # Regular expression pattern for 5-digit US zip codes
    # This pattern looks for 5 consecutive digits that are either:
    # - at the beginning of a string or preceded by a non-digit character
    # - at the end of a string or followed by a non-digit character
    # This helps avoid matching 5 digits that are part of longer numbers
    pattern = r'(?<!\d)\d{5}(?!\d)'
    
    # Find all matches in the text
    zip_codes = re.findall(pattern, text)
    
    return zip_codes

# Example usage
if __name__ == "__main__":
    sample_text = """
    Our main office is located in Beverly Hills, 90210.
    The warehouse is in 10001, New York.
    Please mail your documents to Springfield, IL 62704.
    John's phone number is 555-123-4567 and his customer ID is 123456789.
    """
    
    result = extract_zip_codes(sample_text)
    print(f"Found {len(result)} zip codes: {result}")