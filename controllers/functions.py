

class Function:
    def __init__(self):
        pass
    
    def check_if_digit():
        valid_result = False
        while not valid_result:
            choice = input("--> ")
            try:
                if int(choice):
                    valid_result = True
            except Exception:
                print("\nVous devez entrer un nombre entier")
        return choice
   
    def check_if_positive():
        valid_result = False
        while not valid_result:
            choice = input("--> ")
            try:
                if int(choice) >= 0:
                    valid_result = True
            except Exception:
                print("\nVous devez entrer un nombre positif")
        return choice

    def check_if_not_empty():
        pass

# def main():
    
#     print(Function.check_if_digit())
#     print(Function.check_if_positive()) 

# if __name__ == "__main__":
#     main()
