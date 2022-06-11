"""Есть группа из 100 предметов. Предметы могут быть синего, зелёного и красного цвета. Известно,
что предметов синего цвета сильно больше, чем предметов зелёного цвета, а предметов зелёного цвета немного больше,
чем предметов красного цвета. Напишите сервис, который будет принимать номер предмета и пытаться угадать его цвет.
Логику работы сервиса определите самостоятельно."""
import random


def get_result(number):
    res = random.choices(['blue', 'green', 'red'], weights=[4, 2, 1])
    print(f"item number {number} most likely {res[0]}")

