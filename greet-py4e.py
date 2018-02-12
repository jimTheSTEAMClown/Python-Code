# ============================================================================
# Source: STEAM Clown - www.steamclown.org 
# GitHub: https://github.com/jimTheSTEAMClown/Python-Code
# Hacker: Jim Burnham - STEAM Clown, Engineer, Maker, Propmaster & Adrenologist 
# This example code is licensed under the CC BY-NC-SA 3.0.
# https://creativecommons.org/licenses/by-nc-sa/3.0/
# Program/Design Name:		greet-py4e.py
# Description:    This is a template for passing parameters to a function
# See https://www.py4e.com/lessons/functions
# Dependencies:   python3
# Revision: 
#  Revision 0.02 - Updated 02/11/2018 for SVCTE Mechatronics Class
#  Revision 0.01 - Created 02/11/2018
# Additional Comments: 
  # Edit this code to invoke greet() for spanish
  # Add another language, like Russan, or Swahili
# ============================================================================

def greet(lang):
  if lang == 'es':
    return('Hola')
  elif lang == 'fr':
    return('Bonjour')
  else:
    return('Hello')

def main():
  print(greet('en'),'David')
  print(greet('fr'),'Sabine')
  

# This is the call to the Function main().  You should always 
# have a main() and def main(): as part of all your programs
main()
