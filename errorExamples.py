# ============================================================================
# Source: STEAM Clown - www.steamclown.org 
# GitHub: https://github.com/jimTheSTEAMClown/Python-Code
# Hacker: Jim Burnham - STEAM Clown, Engineer, Maker, Propmaster & Adrenologist 
# This example code is licensed under the CC BY-NC-SA 3.0.
# https://creativecommons.org/licenses/by-nc-sa/3.0/
# Program/Design Name:		errorExamples.py
# Description:    This is an example of errors in python programs
# Dependencies:   python3
# Revision: 
#  Revision 0.02 - Updated 02/4/2018 for SVCTE Mechatronics Class
#  Revision 0.01 - Created 02/4/2018
# Additional Comments: 
# 
# ============================================================================

def main():
   # This is the main function.  all your main code goes here.
   # There are at least 5 errors. Try to find them all   
   print ("This program illustrates a if function“)
   numberFromKeyboard = input("Enter a number between 0 and 9: ")
   newNumber=numberFromKeyboard+1
   if newNumber == 5:
      print('your number is 5')
   
   print('All Done")
   # All done

# This is the call to the Function main().  You should always 
# have a main() and def main(): as part of all your programs
main()
