# ============================================================================
# Source: STEAM Clown - www.steamclown.org 
# GitHub: https://github.com/jimTheSTEAMClown/Python-Code
# Hacker: Jim Burnham - STEAM Clown, Engineer, Maker, Propmaster & Adrenologist 
# This example code is licensed under the CC BY-NC-SA 3.0.
# https://creativecommons.org/licenses/by-nc-sa/3.0/
# Program/Design Name:		aStartingTemplateForClass.py
# Description:             This is a template for python programs
# Dependencies: 
# Revision: 
#  Revision 0.02 - Updated 01/21/2018 for SVCTE Mechatronics Class
#  Revision 0.01 - Created 01/20/2018
# Additional Comments: 
# 
# ============================================================================

def main():
   # Get the name of the file and open it
   name = input('Enter file:')
   handle = open(name, 'r')
   
   # Count word frequency
   counts = dict()
   for line in handle:
      words = line.split()
      for word in words:
         counts[word] = counts.get(word,0) + 1
   
   # Find the most common word
   bigcount = None
   bigword = None
   for word,count in counts.items():
      if bigcount is None or count > bigcount:
         bigword = word
         bigcount = count
   
   # All done
   print(bigword, bigcount)

# This is the call to the Function main().  You should always 
# have a main() and def main(): as part of all your programs
main()
