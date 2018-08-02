def pigLatin():
	suffix1='way'
	suffix2='ay'
	vowel = set("aeiou")
	s=raw_input("Enter the word:")
	if vowel & set(s):
	    if s[0] in vowel:
	      return s+suffix1
	    else:
	      while s[0] not in vowel:
		  s = s[1:] + s[0]
	      return s+suffix2
	    
	else:
	   return "Has no vowel"
	  
print(pigLatin())	  
	  
#unit test.

