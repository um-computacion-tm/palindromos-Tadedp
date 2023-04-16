def isPalindromeIterative(word):
    word = word.lower()
    for i in range(len(word)):
        if word[i] != word[-(i + 1)]:
            return False  
    return True

if __name__ == '__main__':
    pass