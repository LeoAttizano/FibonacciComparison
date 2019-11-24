from os import system
import time


Red='\033[31m'          # Red
Green='\033[32m'        # Green
Yellow='\033[33m'       # Yellow
Blue='\033[34m'         # Blue
Purple='\033[35m'       # Purple
Cyan='\033[36m'         # Cyan
White='\033[37m'        # White


def banner():
    system('clear')
    text = f'''{Green}Different Approaches to Fibonacci{White}\n
        {Yellow}Author: Leonardo C R Attizano{White}\n'''
    print(text)


def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)


def fib_bottom_up(n):
    start = time.time()
    if n == 1 or n == 2:
        print(1)
    bottom_up = [None] * (n+1)
    bottom_up[1] = 1
    bottom_up[2] = 1
    for i in range(3, n+1):
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
    end = time.time()
    elapsed = end - start
    print(f'{Green}Time Elapsed: {Yellow}' + str(elapsed) + f'{Green}s')
    print(f'{Green}The number {Cyan}' + str(n) + f'{Green} of the Fibonacci Sequence is: {Cyan}' + str(bottom_up[n]))


def core():
    while True:
        print(f'{Green}[*] Actions:')
        print(f'{Green}[1] Recurse')
        print(f'{Green}[2] Bottom_up')
        print(f'{Green}[Ctrl+C] - Exit')

        choice = input(f'{Red}[>] {White}')
        print(f'{Green} What number from Fibonacci\'s Sequence are you looking for?')

        if choice == '1':
            n = int(input(f'{Red}[>] {White}'))

            if n <= 0:
                print("Plese enter a positive integer")
            else:
                start = time.time()

                for i in range(n + 1):
                    pass

            end = time.time()
            elapsed = end - start

            print(f'{Green}Time Elapsed: {Yellow}' + str(elapsed) + f'{Green}s')
            print(f'{Green}The number {Cyan}' + str(n) + f'{Green} of the Fibonacci Sequence is: {Cyan}' + str(fib(i)))

        elif choice == '2':
            n = int(input(f'{Red}[>] {White}'))
            if n <= 0:
                print("Plese enter a positive integer")
            else:
                fib_bottom_up(n)
        else:
            print(f'{Red}[-]Invalid Choice{White}\n')
            core()


if __name__ == '__main__':
    try:
        banner()
        core()
    except KeyboardInterrupt:
        print('\nGood Bye!\n')
