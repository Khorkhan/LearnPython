import re
chat_log = "Player1: /heal me, Player2: /warp forest, Player3: Hello!"
commands = re.findall(r"/\w+", chat_log)
print(commands)