data=open('txt_file\data02.txt').read()
def main(data:str):
    """
    The data is from the file. Return number of characters in the file.
    Args:
        data: str
    Returns:
        int: return answer
    """
    return len(data)
print(main(data))
# Read data from file