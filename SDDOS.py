# Fungsi curl,  Kode Python Requests,  Keterangan
# curl https://api.github.com/users/google,  response = requests.get('https://api.github.com/users/google'),  Permintaan GET dasar.
# "curl -X POST -d '{""key"":""value""}' https://httpbin.org/post",  "payload = {'key': 'value'}response = requests.post('https://httpbin.org/post', json=payload)",  Permintaan POST dengan data JSON.
# "curl -H ""Authorization: Bearer token"" https://api.example.com",  "headers = {'Authorization': 'Bearer token'}response = requests.get('https://api.example.com',   headers=headers)",Mengirim Header kustom.


import requests
import threading
import time

# --- Variabel Global ---
# --- EDIT HERE ---
totalTrehad = 3
delay = 0.1
link = 'http://127.0.0.1:8787/'




# --- DONT TOUCH THE BOTTOM CODE IF NOT UNDERSTAND ---





def tugas_thread(thread_id, waktu_tunggu):
    while True:
        time.sleep(waktu_tunggu)
        requests.get(link)

if __name__ == "__main__":
    
    daftar_thread = []

    for i in range(totalTrehad):
        
        time.sleep(0.01)

        thread = threading.Thread(
            target=tugas_thread, 
            args=(i + 1, delay),
            daemon=True
        )
        
        daftar_thread.append(thread)
        
        print(f"[{time.strftime('%H:%M:%S')}] Thread Utama: Memulai thread {i + 1}...")
        thread.start()

    print(f"[{time.strftime('%H:%M:%S')}] Thread Utama: Semua thread sudah dimulai.")
    print(f"Total thread yang aktif saat ini: {threading.active_count()}")
    
while True:
    time.sleep(delay)
    try:
        response = requests.get(link)
        response.raise_for_status()

        print("--- 1. Status Kode (Code Status) ---")
        print(response.status_code)

    except requests.exceptions.RequestException as e:
        print(f"Terjadi kesalahan saat melakukan permintaan: {e}")

