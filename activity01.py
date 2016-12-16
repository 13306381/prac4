__author__ = 'jc458517'

vowels=['a', 'e', 'i', 'o', 'u']
vowels_count=0
name=input("Enter your name:")
for c in name:
    if c.lower() in vowels:
        vowels_count +=1
        print(vowels_count)
        print('Out of {} letters, {} has {} vowels'.format(len(name),name,vowels_count))