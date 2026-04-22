import psutil
from datetime import datetime
from time import sleep

log_file = open('system_log.txt','w')
try:
  while True:
   # Doc CPU
   cpu_list = psutil.cpu_percent(interval=1,percpu=True)
   cpu_avg = sum(cpu_list)/len(cpu_list)
   if cpu_avg>=70:
      status = 'CRITICAL'
   elif cpu_avg>=30:
      status = 'WARNING'
   else:
      status = 'NORMAL'
 # Doc RAM
   ram = psutil.virtual_memory()
   ram_used_mb = ram.used //(1024**2)
   ram_total_mb = ram.total //(1024**2)
   ram_pct = ram.percent

   # Doc disk
   disk = psutil.disk_usage('/')
   disk_pct = disk.percent

   #Dinh dang thoi gian
   now = datetime.now().strftime('%Y-%m-%d-%H:%M:%S')


   # Tao dong output chuan
   line = f'[{now}] CPU: {cpu_avg:.1f}% | RAM: {ram_used_mb}/{ram_total_mb} M>

print(line)
   if status != 'NORMAL':
     print(f' {status}: CPU dang o {cpu_avg:.1f}%')
   log_file.write(line+'\n')
   log_file.flush()

   # Lap lai sau moi 2s
   sleep(2)

except KeyboardInterrupt:
  print('\nDung giam sat.')
finally:
  log_file.close()
  print('Log saved to system_log.txt')
