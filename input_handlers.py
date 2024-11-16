from colorama import Fore

def get_user_input(prompt: str, allow_empty: bool = True) -> str:
    """Get user input with optional empty check"""
    while True:
        value = input(prompt).strip()
        if value or allow_empty:
            return value
        print(f"{Fore.YELLOW}Input required, please try again")

def get_numeric_input(prompt: str, min_val: int = None, max_val: int = None) -> int:
    """Get numeric input with range validation"""
    while True:
        try:
            value = get_user_input(prompt)
            if not value:
                return None
            num = int(value)
            if min_val is not None and num < min_val:
                print(f"{Fore.YELLOW}Value must be at least {min_val}")
                continue
            if max_val is not None and num > max_val:
                print(f"{Fore.YELLOW}Value must be no more than {max_val}")
                continue
            return num
        except ValueError:
            print(f"{Fore.YELLOW}Please enter a valid number")
