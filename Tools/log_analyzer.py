#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Log Analyzer - Скрипт для анализа текстовых логов.
ВНИМАНИЕ! Использовать только для:
1. Анализа собственных логов сервера.
2. Решения CTF-задач (где это разрешено правилами).
3. Тестирования своей инфраструктуры.
"""

import re
from collections import Counter

# --- НАСТРОЙКИ ---
LOG_FILE = 'log.txt'  # Замени на имя твоего файла

def analyze_log(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"[!] Ошибка: Файл '{filename}' не найден.")
        return

    ips = []
    methods = []
    hidden_chars = []

    # Регулярные выражения для поиска
    ip_pattern = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')
    method_pattern = re.compile(r'\b(GET|POST|PUT|DELETE|HEAD|OPTIONS)\b')
    # Ищем паттерн /путь/символ (для сбора флагов по кусочкам)
    hidden_pattern = re.compile(r'/([a-zA-Z0-9_\-\.]+)/([a-zA-Z0-9_\-\.\{\}])')

    for line in lines:
        # Ищем IP
        ip_match = ip_pattern.search(line)
        if ip_match:
            ips.append(ip_match.group())
        
        # Ищем HTTP-методы
        method_match = method_pattern.search(line)
        if method_match:
            methods.append(method_match.group())
            
        # Ищем скрытые символы в конце URL
        hidden_match = hidden_pattern.search(line)
        if hidden_match:
            hidden_chars.append(hidden_match.group(2))

    print(f"--- Анализ файла: {filename} ---")
    print(f"Всего строк: {len(lines)}\n")
    
    print("[+] Топ-5 IP-адресов:")
    for ip, count in Counter(ips).most_common(5):
        print(f"    {ip}: {count} раз")
        
    print("\n[+] Топ-5 HTTP-методов:")
    for m, count in Counter(methods).most_common(5):
        print(f"    {m}: {count} раз")
        
    if hidden_chars:
        print("\n[!] Найдены скрытые символы в URL (собираем флаг):")
        print("    " + "".join(hidden_chars))
    else:
        print("\n[-] Скрытых символов в URL не найдено.")

if __name__ == "__main__":
    analyze_log(LOG_FILE)