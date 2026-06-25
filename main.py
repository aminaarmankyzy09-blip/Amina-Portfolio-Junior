import json
import os
import re
import textwrap


class JuniorPortfolio:
    def __init__(self, content_file):
        self.content_file = content_file
        self.github_link = "https://github.com/aminaarmankyzy09-blip/Amina-Portfolio-Junior"
        self.data = self.load_content()

    def load_content(self):
        # Если файла нет, выводим ошибку
        if not os.path.exists(self.content_file):
            print(f"❌ Файл {self.content_file} не найден!")
            return {}
        try:
            with open(self.content_file, "r", encoding="utf-8") as f:
                content = json.load(f)
                # Подставляем ссылку на гитхаб в текст
                if "github" in content:
                    content["github"] = content["github"].format(github_url=self.github_link)
                return content
        except Exception as e:
            print(f"❌ Ошибка чтения JSON: {e}")
            return {}

    def draw_border(self):
        # Обычная линия для красоты меню
        print("=" * 65)

    def show_menu(self):
        # Вывод главного меню в консоль
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
        # Связываем цифры меню с ключами из файла content.json
        menu_actions = {
            "1": "about_me", "2": "goal", "3": "history", "4": "mentor",
            "5": "point_ab", "6": "hobby", "7": "projects", "8": "github"
        }

        while True:
            self.show_menu()
            choice = input("👉 Введите цифру раздела (0-8): ").strip()

            # Проверка, что введена строго одна цифра от 0 до 8
            if not re.match(r"^[0-8]$", choice):
                print("\n❌ Ошибка! Нужно ввести цифру от 0 до 8.")
                input("\nНажмите Enter...")
                continue

            if choice == "0":
                print("\n👋 Программа завершена. Спасибо за внимание!")
                break

            block_key = menu_actions[choice]
            self.display_block(block_key)

    def display_block(self, key):
        print("\n")
        self.draw_border()
        if key in self.data:
            # textwrap.fill автоматически разбивает текст на строки шириной ровно 65 символов
            formatted_text = textwrap.fill(self.data[key], width=150)
            print(formatted_text)

            # Если открыли пункт 7, автоматически запускаем файлы
            if key == "projects":
                try:
                    print("\n[Система]: Открываю презентацию и фото документов...")
                    os.startfile("my_presentation.pdf")
                    os.startfile("my_document.png")
                except Exception:
                    # Если файлы не нашлись, просто пропускаем ошибку, чтобы код не падал
                    pass
        else:
            print("⚠ Раздел не найден.")
        self.draw_border()
        input("\nНажмите Enter, чтобы вернуться в меню...")


if __name__ == "__main__":
    app = JuniorPortfolio("content.json")
    app.start()