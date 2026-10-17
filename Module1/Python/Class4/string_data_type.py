import os

name = "Usama";
age = 22
# F Strings(String Formatting)
print(f'My Name Is {name} And My Age Is {age}')

os.system('cls')

# ESCAPE SEQUENCES
print(f"My Name Is '{name}' And My Age Is '{age}'")
# print(f'My Name Is {name} And My Age Is '{age}'' )
# Solution
# \' \"
print(f'My Name Is \'{name}\' And My Age Is \'{age}\'')
print(f'My Name Is \'{name}\' And My Age Is \'{age}\'')
# \\
print(f'My Name Is {name}\\ And My Age Is {age}')
print(f'My Name Is {name}\n And My Age Is {age}')
# For Gap (Tab Spacing)
print(f'My Name Is {name}\t And My Age Is {age}')
os.system('cls');
# For Backspace
print(f'My Name Is {name} \bAnd My\b Age Is {age}')
os.system('cls');
txt = 'My Name Is Usama and My Age Is 22'
# To Find
print(txt.find('Usama'));
print(txt[11:15]);
print(txt.rfind('is'))
os.system('cls')
# split (alag alag kar daa na)
print(txt.split('and'))
print(txt.split('and')[1].strip())