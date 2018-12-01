def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)

something = str.lower(input('text: '))#понижение регистра при получении строки

something = something.replace(" ",'')#замена одного символа на другой

if (is_palindrome(something)):
    print('Palindrom')
else:
    print('not Palindrom')
