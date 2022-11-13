data=open('txt_file\data01.txt')
def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    data=data.read()
    return data.split()
print(main(data))
# Read data from file
