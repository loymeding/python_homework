'''
Создайте класс, который будет представлять собой буфер данных. У класса должны быть следующие методы:

add_data(data): добавить данные в буфер. Если в буфере уже есть хотя бы 5 элементов, вывести сообщение о переполнении буфера и очистить его.

get_data(): получить данные из буфера. Если буфер пуст, вывести сообщение об отсутствии данных.
'''


class DataBuffer:
    def __init__(self):
        self.buffer = []

    def add_data(self, data):
        self.buffer.append(data)
        if len(self.buffer) >= 5:
            print("Переполнение буфера! Очистка буфера.")
            self.buffer.clear()

    def get_data(self):
        if not self.buffer:
            print("Буфер пуст. Нет данных для получения.")
            return None
        return self.buffer


if __name__ == "__main__":
    buffer = DataBuffer()

    # Добавляем данные
    for i in range(8):
        buffer.add_data(i)

    # Получаем данные
    data = buffer.get_data()
    if data:
        print("Данные в буфере:", data)
