class Hall:
    def __init__(self, rows, cols, hall_no) -> None:
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no

    def __entry_show__(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self.show_list.append(show_info)
        arr = [[0]*self.cols] * self.rows
        self.seats[id] = arr
class Star_Cinema(Hall):
    hall_list = []
    def __init__(self) -> None:
        pass

    def __entry_hall__(self, rows, cols, hall_no):
        super().__init__(rows, cols, hall_no)
        self.hall_list.append(self)

cinema = Star_Cinema()
cinema.__entry_hall__(5, 5, 11)

def input_show_entry():
    id = str(input('Enter show ID: '))
    name = str(input('Enter show name: '))
    time = str(input('Enter show time: '))
    cinema.hall_list[0].__entry_show__(id, name, time)
    for hall in cinema.hall_list:
        print(hall.seats)
        print(hall.show_list, hall.rows, hall.cols)
        # hall.
        # print(hall.show_list[id])
        # for show in hal.
# for hall in cinema.hall_list:
#     print(hall.rows, hall.cols , hall.hall_no, hall.show_list)

input_show_entry()
# input_show_entry()
