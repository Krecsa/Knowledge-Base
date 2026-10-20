#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Base64 Decoder - Универсальный декодер для куки и токенов.
Используется для анализа данных, которые видит браузер.
"""

import base64
import json

def decode_base64():
    encoded_str = input("Введите строку Base64 (например, eyJ...): ").strip()
    
    if not encoded_str:
        print("[!] Пустая строка.")
        return

    # Добавляем padding (символы =), если их нет
    missing_padding = len(encoded_str) % 4
    if missing_padding:
        encoded_str += '=' * (4 - missing_padding)
        
    try:
        decoded_bytes = base64.b64decode(encoded_str)
        decoded_str = decoded_bytes.decode('utf-8', errors='replace')
        
        print("\n--- Результат (Текст) ---")
        print(decoded_str)
        
        # Если это JSON, выводим красиво
        try:
            parsed_json = json.loads(decoded_str)
            print("\n--- Результат (JSON) ---")
            print(json.dumps(parsed_json, indent=4, ensure_ascii=False))
        except json.JSONDecodeError:
            pass  # Это не JSON, просто текст
            
    except Exception as e:
        print(f"[!] Ошибка декодирования: {e}")

if __name__ == "__main__":
    decode_base64()