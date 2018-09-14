def cigar_party(cigars, is_weekend):
  
  if(is_weekend == False):
    if(40<=cigars<=60):
      return True
    else:
      return False
  else:
    if(40<=cigars):
      return True
    else:
      return False
