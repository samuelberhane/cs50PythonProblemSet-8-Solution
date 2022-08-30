from datetime import date
import re
import sys
import inflect
p = inflect.engine()


def main():
    birth_date = input("Date of Birth: ")
    print(total_min(birth_date))
    
    
def total_min(birth_date):
    try:
        check_birth_date(birth_date)
        year,month,day = birth_date.split("-")
        date_of_birth = date(int(year),int(month),int(day))
        today = date.today()
        min_diff = today - date_of_birth 
        birth_min = min_diff.days * 24 * 60
        min_word = p.number_to_words(birth_min, andword = "")
        return (f"{min_word.capitalize()} minutes")   
    except:
        sys.exit("Invalid date")


def check_birth_date(birth_date):
       if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$",birth_date):
        return birth_date
        
    
if __name__ == "__main__":
    main()