def autoVal(user,passw):
    def passTst(user,passw):
        if len(user)<5:
            print('username is too small')
        elif (len(passw)>8)==False:
            print('legnth of password is too small')
        elif any([letter.isupper() for letter in passw]) == False:
            print('password should contain atleast one capital letter')
        elif any([letter.islower() for letter in passw]) == False:
            print('password should contain atleast one small letter')
        elif any([letter.isdigit() for letter in passw]) == False:
            print('password should contain atleast one number')
        elif(('@'or'#'or'$'or'%'or'^'or'&'or'*'or'('or')'or'+'or'-'or'!'or'/'or'.'or'>'or'<'or','or'['or']'or'='or'_') in passw)==False:
            print('password should contain atleast one special character')
        else:
            print('valid password')

    passTst(user,passw)
