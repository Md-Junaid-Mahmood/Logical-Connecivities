# Logical-Connecivities
The aim of this repository is to practice Python Programming on few logical connectivities
Basically five types of explicit logical connectivities are used in above files
They are:
  AND
  OR
  NOT
  IMPLY
  BiDIRECTIONALIMPLY
  
Above set of insructions are made to interact with the user using a command line interface
Symbols which are to be used in the logic statement are user defined. User is supposed to enter the symbol (English words) along with their proper description
Sentences can be constructed using above designed symbols. However, the limitation is that one can use only two symbols at a time to construct a sentence
User can then construct a knowledge-base using this set of sentences

Above set of code also consist of Model Checking Algorithm using which one can assert about the truthness of a symbol based on the given knowledge base
The only input which above algorithm requires from the user is the symbol whose truthness is to be evaluated
The symbol is evaluated to be true, if it comes out to be true on each and every model for which our knowledge-base is true
Model represents a possible world where each symbol is assigned a truth value
If there are n symbols used in our knowledge-base, then there can be 2^n possible models

Finally, the above program is an attempt to get started with Python Programming Language
