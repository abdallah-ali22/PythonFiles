def translateToZ(str):
    vol = 'aeiou'
    result = ""
    for letter in str:
        if letter.lower() in vol:
            if letter.isupper():
                result = result + 'Z'
            else:
                result = result + 'z'
        else:
            result = result + letter
        
    return result



# text = "My Name is Islam"
text = "COdeZIlLa"
print(translateToZ(text))