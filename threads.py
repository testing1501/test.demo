import threading

class Messanger(threading.Thread):
    def run(self):
        for _ in range(10):
            print("My name is %s"%self.name)

receive = Messanger(name="Receive")
send = Messanger(name="Send")

receive.start()
send.start()