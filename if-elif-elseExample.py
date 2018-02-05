# ============================================================================
# Source: STEAM Clown - www.steamclown.org 
# GitHub: https://github.com/jimTheSTEAMClown/Python-Code
# Hacker: Jim Burnham - STEAM Clown, Engineer, Maker, Propmaster & Adrenologist 
# This example code is licensed under the CC BY-NC-SA 3.0.
# https://creativecommons.org/licenses/by-nc-sa/3.0/
# Program/Design Name:		if-elif-elseExample.py
# Description:    This is an example of "if" structure for python programs
# Dependencies:   python3
# Revision: 
#  Revision 0.02 - Updated 04/4/2018 for SVCTE Mechatronics Class
#  Revision 0.01 - Created 02/4/2018
# Additional Comments: 
# 
# ============================================================================
def myCoolFunction(a):
   print (type(a))
   print(a)
   if a == '1':
      print ('this is the character 1')
   elif a == '2':
      print ('this is the character 2')
   else: 
      print ('this is the character 3') # Is this right? What about 4,5,6...

def main():
   # This is the main function.  all your main code goes here.  
   print ('This program illustrates a if / else / else if function')
   
   myCoolFunction(input('input:'))
   
   print('back from myCoolFunction')
   print('All Done')
   # All done

# This is the call to the Function main().  You should always 
# have a main() and def main(): as part of all your programs
main()
