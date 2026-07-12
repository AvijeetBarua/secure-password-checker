from app import password_strenght

def test_password_logic():
    print("Running tests for password strength logic...")
    
    assert password_strenght("123456") == "WEAK 🔴"
    assert password_strenght("WINTER2021") == "MEDIUM 🟡"
    assert password_strenght("Summer2021!") == "STRONG 🟢"
    
    print("All tests passed! 🟢")
    
if __name__ == "__main__":
    test_password_logic()