#! python3
# phoneAndEmail.py - Fids phone numbers and emails on the clip

import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?          #area code
    (\s|-|\.)?                  #dash (option)
    (\d{3})                     #beginning digits
    (\s|-|\.)?                  #dash (option)
    (\d{4})                     #id digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))? #added digits (option)
    )''',re.VERBOSE)

#TODO: implement email regex.
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+       #username
    @                                         #@ symbol
    [a-zA-Z0-9.-]+              #domain name
    (\.[a-zA-Z]{2,4})         #.something
    )''', re.VERBOSE)

#TODO: implement find method for clip
stringToSearch = str(pyperclip.paste())
finds = []
for groups in phoneRegex.findall(stringToSearch):
        phoneNum = '-'.join([groups[1], groups[3],groups[5]])
        if groups[8] != '':
            phoneNum += '  line' + groups[8]
        finds.append(phoneNum)
for groups in emailRegex.findall(stringToSearch):
    finds.append(groups[0])


#TODO: copy results to clip
if len(finds) > 0:
    pyperclip.copy('\n'.join(finds))
    print('Copied to clipboard:')
    print('\n'.join(finds))
else:
    print('No phone numbers /emails found.')



    






