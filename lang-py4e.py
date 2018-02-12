# ============================================================================
# Source: STEAM Clown - www.steamclown.org 
# GitHub: https://github.com/jimTheSTEAMClown/Python-Code
# Hacker: Jim Burnham - STEAM Clown, Engineer, Maker, Propmaster & Adrenologist 
# This example code is licensed under the CC BY-NC-SA 3.0.
# https://creativecommons.org/licenses/by-nc-sa/3.0/
# Program/Design Name:		lang-py4e.py
# Description:    This is a template for passing parameters to a function
# See https://www.py4e.com/lessons/functions
# Dependencies:   python3
# Revision: 
#  Revision 0.02 - Updated 02/11/2018 for SVCTE Mechatronics Class
#  Revision 0.01 - Created 02/11/2018
# Additional Comments: 
# 
# ============================================================================

def greet(lang):
  if lang == 'es':
    print('Hola')
  elif lang == 'fr':
    print('Bonjour')
  else:
    print('Hello')

def main():
  greet('en')
  greet('fr')
  

# This is the call to the Function main().  You should always 
# have a main() and def main(): as part of all your programs
main()
