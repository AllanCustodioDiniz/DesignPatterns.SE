class Observer:
    def update(self, message):
        pass

class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

class EmailNotifier(Observer):
    def update(self, message):
        print(f"Enviando email: {message}")

class SMSNotifier(Observer):
    def update(self, message):
        print(f"Enviando SMS: {message}")

def main():
    subject = Subject()
    email_notifier = EmailNotifier()
    sms_notifier = SMSNotifier()

    subject.attach(email_notifier)
    subject.attach(sms_notifier)

    subject.notify("Nova mensagem chegou!")  # Saída: Enviando email: Nova mensagem chegou! e Enviando SMS: Nova mensagem chegou!

if __name__ == "__main__":
    main()
