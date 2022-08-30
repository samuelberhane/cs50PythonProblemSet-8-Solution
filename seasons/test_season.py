from season import check_birth_date,total_min

def main():
    test_valid_birthday()
    test_total_min()
    
def test_valid_birthday():
    assert check_birth_date('1995-03-21') == "1995-03-21"
    assert check_birth_date("1994-7-8") == None
    assert check_birth_date("May 21, 1995") == None
    
def test_total_min():
    assert total_min("1995-03-21") == "Fourteen million, four hundred thirty thousand, two hundred forty minutes"
    assert total_min("2000-01-01") == "Eleven million, nine hundred fourteen thousand, five hundred sixty minutes"
   
    
if __name__ == "__main__":
    main()
    
    