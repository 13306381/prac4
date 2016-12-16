__author__ = 'jc458517'
num=0
out_file=open("numbers.txt","w")
while num >=0:
  num= int(input("number:"))
  if num >=0:
   print(str(num),file=out_file)
out_file.close()