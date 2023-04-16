from palindromeRecursive import isPalindromeRecursive

def isPalindromePhrase(phrase):
    word = ""
    for i in range(0,len(phrase)):
        if phrase[i].isalpha():
            word = word + phrase[i]
            
    return isPalindromeRecursive(word) 

if __name__ == '__main__':
    pass