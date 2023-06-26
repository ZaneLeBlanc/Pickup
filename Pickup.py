#Data dictionaries
Titans = {"Ion": 1, "Tone": 1, "Monarch":1, "Ronin":1, "Northstar":1, "Legion":1, "Scorch":1}
Ordnances = {"Gravity Star": 1, "Satchel":1, "Firestar":2, "Arc Grenade":1, "Frag Grenade":1, "Electric Smoke":1}

def start():
  print ('enter "help" for list of commands and symbols \n' )
  print ("Available Titans:\n Ion - - - - i\n Tone - - -  t\n Monarch - - m\n Ronin - - - r\n Northstar - n\n Legion - -  l\n Scorch - -  s\n \nAvailable Ordnances:\n Gravity Star - - g\n Satchel - - - -  s\n Firestars (2) - - fs\n Arc Grenade - -  a\n Frag Grenade - - f\n Electric Smoke - e\n" )

def printAvailable():
  print(chr(27)+'[2j')
  print('\033c')
  print('\x1bc')
  print ('enter "help" for list of commands and symbols\n')
  print ("******Available Titans:******")
  for titan in Titans:
    if Titans[titan] > 0:
      print (titan)
  print()
  print()
  print ("******Available Ordnances******")
  for ordnance in Ordnances:
    if Ordnances[ordnance] > 0:
      print (ordnance)
  print ()

def resetData():
  Titans = {"Ion": 1, "Tone": 1, "Monarch":1, "Ronin":1, "Northstar":1, "Legion":1, "Scorch":1}
  Ordnances = {"Gravity Star": 1, "Satchel":1, "Firestar":2, "Arc Grenade":1, "Frag Grenade":1, "Electric Smoke":1}

def printHelpCommands():
  print("---------------------------------------------------------")
  print("r >>> resets program")
  print("symbols >>> shows input symbols")
  print("\n-To remove a single item, enter 'null' or 'no' for the symbol of the item not being changed\nex: removing just a frag grenade would look like: 'no f'")
  print("\n-All input in converted to lowercase, so your interactions are not case sensitive")
  print("---------------------------------------------------------")
  print()

#START OF PROGRAM?


while True:
  printAvailable()

  #collect user input
  x = input("Enter titan and ordnance: (TitanSymbol OrdnanceSymbol)").lower()
  xs = x.split()

  # process reset and help
  if x == "r": #make a condition to detect "reset" as keyword as well
    resetData()
    printAvailable()
    continue
  elif x == "help":
    printHelpCommands()
    continue
  elif x == "symbols":
    print ("\n Ion - - - - i\n Tone - - -  t\n Monarch - - m\n Ronin - - - r\n Northstar - n\n Legion - -  l\n Scorch - -  s\n \n Gravity Star - - g\n Satchel - - - -  s\n Firestars (2) - - fs\n Arc Grenade - -  a\n Frag Grenade - - f\n Electric Smoke - e\n")
    continue
  print("---------------------------------------------------------")
 
  #Input Conversion
  #Titan input conv
  # make this into a separate function?
  try:
    if xs[0] == "i" or xs[0] =="ion":
      xs[0] = "Ion"
    elif xs[0] == "t" or xs[0] =="tone":
      xs[0] = "Tone"
    elif xs[0] == "m" or xs[0] =="monarch":
      xs[0] = "Monarch"
    elif xs[0] == "r" or xs[0] =="ronin":
      xs[0] = "Ronin"
    elif xs[0] == "n" or xs[0] =="northstar" or xs[0] =="ns":
      xs[0] = "Northstar"
    elif xs[0] == "l" or xs[0] =="legion":
      xs[0] = "Legion"
    elif xs[0] == "s" or xs[0] =="scorch":
      xs[0] = "Scorch"  
    elif xs[1] == "null" or xs[1] == "no":
      xs[1] == "no"
  except:
    print ("INPUT ERROR, please re-enter that")   
    continue

  #Ordnance input conv
  try:
    if xs[1] == "g" or xs[1] =="gravity" or xs[1] =="grav" or xs[1] =="gs" or xs[1] == "gravs":
      xs[1] = "Gravity Star"
    elif xs[1] == "s" or xs[1] =="satchel" or xs[1] =="sat" or xs[1] =="satchels":
      xs[1] = "Satchel"
    elif xs[1] == "fs" or xs[1] =="firestar" or xs[1] =="fire" or xs[1] =="fstar":
      xs[1] = "Firestar"
    elif xs[1] == "a" or xs[1] =="arc" or xs[1] =="arcgrenade" or xs[1] =="arcs":
      xs[1] = "Arc Grenade"
    elif xs[1] == "f" or xs[1] =="frag" or xs[1] =="frags" or xs[1] =="fraggrenade":
      xs[1] = "Frag Grenade"
    elif xs[1] == "e" or xs[1] =="smoke" or xs[1] =="smokes" or xs[1] =="esmoke":
      xs[1] = "Electric Smoke"
    elif xs[1] == "null" or xs[1] == "no":
      xs[1] == "no"
  except:
    print ("INPUT ERROR, please re-enter")
    continue
  
  #Subtract input from data
  for titan in Titans:
    if xs[0] == titan:
      if (Titans[titan] -1) >= 0:
        Titans[titan] -=1
      else:
        print ("Titan is already taken")
    elif xs[1] == "no":
      pass

  for ordnance in Ordnances:
    if xs[1] == ordnance:
      if (Ordnances[ordnance] -1) >= 0:
        Ordnances[ordnance] -=1
      else:
        print ("Ordnance is already taken")
    elif xs[1] == "no":
      pass

  #Display Results
  printAvailable()

