import random
import string


def getdata():
    """
    Generates a message with upto 100 characters
    @return return string with upto 100 character
    """
    random_num = random.randint(1,100)
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(random_num))


if __name__=="__main__":
    getdata()
    
    