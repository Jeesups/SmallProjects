class NumberLocker():
    def __init__(self, inputedNumber,locker_number):
        self.lock_number = locker_number
        self.input_number = inputedNumber
        self.is_locked = True

        self.checkNumber()
    def checkNumber(self):
        if(self.input_number == self.lock_number):
            self.unlock()
        else:
            self.lock()
    def unlock(self):
        print("Locker is unlocked")
        self.is_locked = True
    def lock(self):
        print("Locker is locked")
        self.is_locked = False


if __name__ == "__main__":
    number = input("Please give locker number to open locker \n")
    app = NumberLocker(number,"123123")