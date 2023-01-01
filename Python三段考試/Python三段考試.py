import random

def play_game(dice):
    result = ""
    # 計算點數
    points = sum(dice)
    # 檢查是否是Sip-Pat
    if points == 10:
        result = "Sip-Pat（10點）！"
    # 檢查是否是一色
    elif all(x == dice[0] for x in dice):
        result = "一色！"
    # 其他情況
    else:
        result = f"{points}點。"
    return result

# 無限迴圈
while True:
    # 生成四個隨機數字
    dice = [random.randint(1, 6) for _ in range(4)]
    # 玩遊戲
    result = play_game(dice)
    # 輸出結果
    print(f"擲出：{dice}")
    print(f"結果：{result}")
    print("輸人Q或q結束；按Ent er重來。")
    # 等待用戶輸入
    user_input = input()
    # 如果用戶輸入Q或q，則退出循環
    if user_input.upper() == 'Q':
        break


