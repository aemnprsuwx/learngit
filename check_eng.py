def check_eng(str)
   strlen=len(str)
   cnt=0
   for i in str:
   if i>='a' and i<='z' or (i>='A' and i<='Z'):
     continue
   elif i>='0' and i<='9':
     continue
   else:
     cnt+=1
   ans=cnt/strlen
   if ans>=0.2:
     return True
   else:
     return False

