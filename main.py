import json
import os
import re


class JuniorPortfolio:
    def __init__(self, content_file):
        """Инициализация и установка ссылки на GitHub"""
        self.content_file = content_file
        # Ссылка на твой репозиторий
        self.github_link = "https://github.com/aminaarmankyzy09-blip/Amina-Portfolio-Junior"
        self.data = self.load_content()

    def load_content(self):
        """Безопасное чтение JSON и подстановка ссылки"""
        if not os.path.exists(self.content_file):
            print(f"❌ Ошибка: Файл {self.content_file} не найден в папке проекта!")
            return {}
        try:
            with open(self.content_file, "r", encoding="utf-8") as f:
                content = json.load(f)
                if "github" in content:
                    content["github"] = content["github"].format(github_url=self.github_link)
                return content
        except Exception as e:
            print(f"❌ Ошибка при чтении файла контента: {e}")
            return {}

    def draw_border(self):
        """Красивый графический разделитель меню"""
        print("=" * 65)

    def show_menu(self):
        """Оформленное текстовое меню"""
        self.draw_border()
        print("👑  КОНКУРСНОЕ ПОРТФОЛИО «ОБО МНЕ» | АМИНА АРМАНКЫЗЫ  👑")
        self.draw_border()
        print("[1] 📑 О себе                      [2] 🎯 Моя цель")
        print("[3] 🚀 Как я пришла в IT           [4] 🤝 Мой ментор (Аида)")
        print("[5] 📍 Точка А -> Точка Б          [6] 🎈 Хобби и настольные игры")
        print("[7] 💻 Мои лучшие работы           [8] 🔗 Ссылка на GitHub")
        print("[0] ❌ Выход из портфолио")
        self.draw_border()

    def start(self):
        """Основной цикл управления меню (while) с валидацией ввода через Regex"""
        menu_actions = {
            "1": "about_me", "2": "goal", "3": "history", "4": "mentor",
            "5": "point_ab", "6": "hobby", "7": "projects", "8": "github"
        }

        while True:
            self.show_menu()
            choice = input("👉 Введите цифру раздела (0-8): ").strip()

            if not re.match(r"^[0-8]$", choice):
                print("\n❌ ОШИБКА ВВОДА! Разрешены только цифры от 0 до 8. Попробуйте еще раз.")
                input("\nНажмите Enter...")
                continue

            if choice == "0":
                print("\n👋 Программа завершена. Спасибо за внимание и оценку проекта!")
                break

            block_key = menu_actions[choice]
            self.display_block(block_key)

    def display_block(self, key):
        """Вывод выбранного блока информации и запуск файлов"""
        print("\n")
        self.draw_border()
        if key in self.data:
            print(self.data[key])

            # Автоматическое открытие файлов при выборе пункта 7
            if key == "projects":
                try:
                    print("\n[Система]: Запускаю PDF-презентацию и фото документов...")
                    os.startfile("my_presentation.pdf")
                    os.startfile("my_document.png")
                except Exception as e:
                    print(f"\n[!] Не удалось автоматически открыть файлы: {e}")
        else:
            print("⚠ Ошибка: Данный раздел не найден в файле контента.")
        self.draw_border()
        input("\nНажмите Enter, чтобы вернуться в главное меню...")


if __name__ == "__main__":
    # Запуск приложения
    app = JuniorPortfolio("content.json")
    app.start()