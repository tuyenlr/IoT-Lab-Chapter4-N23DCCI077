import psutil
from datetime import datetime
from time import sleep

# Mo file de ghi
log_file = open('system_log.txt', 'w')

try:
    while True:
        # 1. Doc thong so CPU
        cpu_list = psutil.cpu_percent(interval=1, percpu=True)
        cpu_avg = sum(cpu_list) / len(cpu_list)

        if cpu_avg >= 70:
            status = 'CRITICAL'
        elif cpu_avg >= 30:
            status = 'WARNING'
        else:
            status = 'NORMAL'

        # 2. Doc thong so RAM
        ram = psutil.virtual_memory()
        ram_used_mb = ram.used // (1024**2)
        ram_total_mb = ram.total // (1024**2)

        # 3. Dinh dang thoi gian
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # 4. Tao dong output
        line = f'[{now}] CPU: {cpu_avg:.1f}% | RAM: {ram_used_mb}/{ram_total_mb} MB'

        # 5. In ra man hinh
        print(line)
        if status != 'NORMAL':
            print(f' {status}: CPU dang o {cpu_avg:.1f}%')

        # 6. Ghi vao file
        log_file.write(line + '\n')
        log_file.flush()

        # 7. Nghi 2 giay roi moi lap lai
        sleep(2)

except KeyboardInterrupt:
    print('\nDung giam sat.')
finally:
    log_file.close()
    print('Log saved to system_log.txt')
