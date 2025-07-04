import readline

class PortableAssistant:
    def __init__(self):
        self.running = True

    def greet(self):
        print("Привет! Я ваш Portable Assistant.")

    def help(self):
        print("Доступные команды: greet, exit, help")

    def run(self):
        self.greet()
        while self.running:
            try:
                command = input("> ").strip()
            except (EOFError, KeyboardInterrupt):
                print()
                break
            if command == "greet":
                self.greet()
            elif command == "help":
                self.help()
            elif command in {"exit", "quit"}:
                self.running = False
            elif command:
                print(f"Неизвестная команда: {command}")


def main():
    assistant = PortableAssistant()
    assistant.run()


if __name__ == "__main__":
    main()
