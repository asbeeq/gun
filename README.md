Файлы и код CV проекта "gun"

Weapon detection image format

1. Возникшие проблемы и пути решения:
а. Проблема с google colab. При запуске обработки моделей, возникает ситуация когда эксперименты моделей прерываются и все данные очищаются.
Например, при 100 экспериментов, обычно 73 экспериментов только обрабатываются. Решение проблемы: Подключить гугл диск:
    from google.colab import drive
    drive.mount('/content/gdrive')
б. Проблема в рантайме использование cpu. Это делало обработку модели долгой. Решение: рантайм установить GPU
2. Обработанная модель, вместе с тестовыми даннными из папки data: https://drive.google.com/drive/folders/1mNxOcyELh81qY82_4E8ivwTdLN8gguML?usp=sharing

Запуск:
1. python weapon_detection.py
2. Следовать инструкции по консоли

Open source contributers:
- Islyambek Kairov
- Assylbek Zakrikchinov
