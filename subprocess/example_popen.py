from subprocess import Popen as p
import subprocess
from time import sleep

# -----------------
# process = subprocess.Popen(['ping', 'ya.ru'])
# process = p(['ls', '-l'])
# print('start ping')

# заблокирует выполнение питон скрипта
# code = process.wait()
# print(code)

# ------------------
# process = subprocess.Popen('./script')
# while process.poll() is None:
#     # пока статус выполнения не станет 0
#     print('script status:', process.poll())
#     sleep(1)
# print('process result: ', process.poll())

# ----------
process = subprocess.Popen(['ping', 'ya.ru'])
print('start ping')
print('process pid: ', process.pid)
sleep(5)
process.kill()
print('process')
