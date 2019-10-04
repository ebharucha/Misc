# import numpy as np
# import matplotlib.pyplot as plt

# x = np.linspace(-10,10)
# y = x**2

# plt.figure(figsize=(20,10))

# plt.plot(x, y, 'r')

# plt.show()

def pallindrometest(s):
    s = s.lower()
    for i in range(len(s)//2):
        if (s[i] == s[-1-i]):
            status = True
        else:
            status = False
            break
    return (status)

def main():
    s = input ('Input the string to test: ')
    if (pallindrometest(s)):
        print (f'"{s}" is a pallindrome')
    else:
        print (f'"{s}" is not a pallindrome')

if __name__ == "__main__":
    main()