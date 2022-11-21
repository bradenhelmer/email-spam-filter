link = ['www.google.com', 'www.yahoo.com', 'www.youtube.com']
email = 'This is a test text string. In this string you will find the algorthm used by www.yahoo.com and www.youtube.co'
spam = False
for i in link:
    if i in email:
        spam = True
    else:
        pass

if spam is False:
    print("Safe Email")
else:
    print("Spam Email")
