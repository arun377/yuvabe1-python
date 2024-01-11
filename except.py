try:
   
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    
    result = numerator / denominator
    
  
    print("Result:", result)

except ValueError:
    print("Please enter valid integers for numerator and denominator.")

except ZeroDivisionError:
    print("Cannot divide by zero. Please enter a non-zero denominator.")

except Exception as e:
    print(f"An error occurred: {e}")

else:
    print("No exceptions occurred.")

finally:
    print("Finally block always executes.")