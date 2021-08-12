# Домашнее задание №33. Цифровой счетчик
class DigtalCounter:
    def __init__(self, min_value=0, max_value=100, current_value= None):
        self.min_value = min_value
        self.max_value = max_value
        if current_value is None:
            self.current_value = self.min_value
        else:
            self.current_value = current_value

    def make_step(self, step =1):
        step = abs(step)
        if self.current_value >= self.max_value:
            self.current_value = self.min_value
        else:
            self.current_value += step

    def get_current_value(self):
        return self.current_value


x = DigtalCounter(1,60)
print(x.current_value)

x.make_step()
x.make_step()
x.make_step()
x.make_step()
x.make_step()

print(x.current_value)