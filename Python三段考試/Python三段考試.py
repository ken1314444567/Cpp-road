#1.使用Try
while True:
    try:
        x = int(input("請輸入一整數為被除數："))
        y = int(input("請輸入一整數為除數："))
        if y == 0:
            print("輸入除數不可為 0!")
        else:
            print("商=", x / y)
            print("餘數=", x % y)
    except ValueError:
        print("輸入資料型別有誤！")
    except EOFError:
        print("發生錯誤！")
    end = input("結束計算？（Y/y）")
    if end.lower() == "y":
        break
#2.計算時間
import time
input("按Enter鍵，開始計時。 ")
start_time = time.time()
input("按Enter鍵，結束計時。  ")
end_time = time.time()
elapsed_time = end_time - start_time
print(f"經過時間為： {elapsed_time:.15f} 秒")
#3.取得現在的時間
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
second = now.second
am_pm = 'AM'
if hour > 12:
    hour -= 12
    am_pm = '下午'
elif hour == 12:
    am_pm = '下午'
print(f"現在時刻：{am_pm} {hour} 時 {minute} 分 {second} 秒")
#4.菱形
def diamond(n):
  if n < 3 or n % 2 == 0:
    return
  for i in range(n):
    num_spaces = abs(n // 2 - i)
    num_stars = n - 2 * num_spaces
    print(" " * num_spaces + "*" * num_stars)
n = int(input("請輸入一個大於等於3的奇數："))
diamond(n)
#5.十八仔
import random
def play_game(dice):
    result = ""
    points = sum(dice)
    if points == 10:
        result = "Sip-Pat（10點）！"
    elif all(x == dice[0] for x in dice):
        result = "一色！"
    else:
        result = f"{points}點。"
    return result
while True:
    dice = [random.randint(1, 6) for _ in range(4)]
    result = play_game(dice)
    print(f"擲出：{dice}")
    print(f"結果：{result}")
    print("輸人Q或q結束；按Enter重來。")
    user_input = input()
    if user_input.upper() == 'Q':
        break
#6.撲克牌花色整理
import random
import collections
deck = [('黑桃', i) for i in range(1, 14)] + [('紅心', i) for i in range(1, 14)] + [('方塊', i) for i in range(1, 14)] + [('梅花', i) for i in range(1, 14)]
hand = random.sample(deck, 5)
suit_dict = collections.defaultdict(list)
for card in hand:
      suit_dict[card[0]].append(card[1])
print("發牌:", hand)
print("整理:", dict(suit_dict))
#7.隨機數抽取
import random
n = 12  
random_numbers = [random.randint(1, 10) for _ in range(n)]
numbers = set(random_numbers)
print("產生的隨機數如下：")
print(random_numbers)
print("其中的數字為：")
print(numbers)  








