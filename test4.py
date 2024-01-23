import pyautogui as auto
from time import sleep

def main():
    input('start')
        # vids = []
    # imgs = []

    # with open('vid_urls.txt', 'r') as f:
    #     mx = int(f.readline())
    #     i = 1
    #     while i < mx:
    #         vids.append(f.read(i))
    #         i += 1

    #     print(vids)


    f = open('vid_urls.txt', 'r')
    lines =  []
    for line in f:
        line = line.strip()
        lines.append(line)
    print(lines)
    f.close()


    auto.press("winright")
    sleep(0.2)
    auto.write("cmd")
    sleep(0.2)
    auto.press('return')
    sleep(0.4)
    auto.write('firefox')
    sleep(0.2)
    auto.press('return')
    sleep(2)

    i = 1
    while i < int(lines[0]):
        print(lines[i])
        auto.write(lines[i])
        sleep(2)
        auto.press('return')
        sleep(0.3)
        auto.click(x=950, y=100)
        sleep(0.2)
        i+=1

    


if __name__ == "__main__":
    main()