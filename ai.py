#najítí všech tras(path,start,end) ->trasy
#začít na startu a jít po barevnejch pixelech. každé rozdvojení vytváří novou cestu
#   pohyb enemáků(trasy) ->pohyb vektor

#může věž střílet(věž,enemak) ->bool
#vyslat fake projektil a zjistit jestli tam není zeď

#jakým směrem střílet(věž,enemak) ->vektor
#   jak dlouho to poletí na současnou polohu
#   posunout enemaka o ten čas vrátit jeho směr od věže