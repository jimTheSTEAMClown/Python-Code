# ============================================================================
# Source: STEAM Clown - www.steamclown.org 
# GitHub: https://github.com/jimTheSTEAMClown/Python-Code
# Hacker: Jim Burnham - STEAM Clown, Engineer, Maker, Propmaster & Adrenologist 
# This example code is licensed under the CC BY-NC-SA 3.0.
# https://creativecommons.org/licenses/by-nc-sa/3.0/
# Program/Design Name:		aTemplate2.py
# Description:    This is a template for python programs.  It shows passing variables 
#                 to a function
# Dependencies:   python3
# Revision: 
#  Revision 0.02 - Updated 01/21/2018 for SVCTE Mechatronics Class
#  Revision 0.01 - Created 01/20/2018
# Additional Comments: 
# 
# ============================================================================

# this is myFunction, which is called from main
def myFunction(myx,myy,z):
  print("\tjust entered myFunction")
  z=z+(myx-myy)+7
  print("\tz=z+(myx-myy)+7 and is now =",z)
  print("\tbut is it really? Think Local vs Global")
  print('\tall done with myFunction')

def main():
  # This is the main function.  all your main code goes here.  
  # You can call other functions from here
  print('starting main')
  #x=2
  x = int(input('Enter value for x between 0-9: '))
  y=6
  z=x+y
  print("x =",x,"y =",y,"z =",z)
  print("calling myFunction with passing variables")
  myFunction(x,y,z)
  print('back in main')
  print("z still =",z)
  print('all done with main')
  # All done

# This is the call to the Function main().  You should always 
# have a main() and def main(): as part of all your programs
main()
