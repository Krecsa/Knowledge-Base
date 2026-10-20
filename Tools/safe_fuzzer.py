#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Safe Fuzzer - Поиск скрытых страниц и файлов.
ВНИМАНИЕ! Использовать только для:
1. Тестирования своих собственных сайтов.
2. Решения CTF-задач (где это разрешено).
3. Проверки инфраструктуры с письменного разрешения владельца.
"""

import requests
import time

# --- НАСТРОЙКИ ---
TARGET_URL = "http://task.duckerz.ru:21003/"  # Замени на свой URL!
PATHS = [
    "admin", "admin.php", "login", "dashboard", "flag", "flag.php",
    "robots.txt", "backup.zip", "index.php.bak", ".git/config", ".env",
    "api", "api/v1", "secret", "config.php", "test", "dev"
]

def fuzz_paths():
    print(f"--- Сканирование {TARGET_URL} ---")
    print(f"--- Проверяем {len(PATHS)} путей ---")
    
    # Честный User-Agent, чтобы не скрываться
    headers = {
        "User-Agent": "MySafeFuzzer/1.0 (Educational CTF Tool)"
    }
    
    for path in PATHS:
        url = f"{TARGET_URL.rstrip('/')}/{path}"
        try:
            # Делаем запрос с таймаутом, чтобы не вешать сервер
            r = requests.get(url, headers=headers, timeout=5, allow_redirects=False)
            
            # Если статус 200 (ОК), 403 (Запрещено), 401 (Требуется авторизация)
            if r.status_code in [200, 403, 401]:
                print(f"[+] Найдено: {url} (Статус: {r.status_code})")
            
        except requests.exceptions.RequestException:
            # Игнорируем ошибки сети (таймауты, недоступность)
            pass
        
        # Пауза между запросами, чтобы не перегружать сервер
        time.sleep(0.5)
        
    print("--- Сканирование завершено ---")

if __name__ == "__main__":
    fuzz_paths()