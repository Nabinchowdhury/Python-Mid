class Hall:
    def __init__(self, rows, cols, hall_no) -> None:
        self.seats = []
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no

class Star_Cinema(Hall):
    hall_list = []
    def __init__(self) -> None:
        pass

    def entry_hall(self, rows, cols, hall_no):
        super().__init__(rows, cols, hall_no)
        self.hall_list.append(self)

cinema = Star_Cinema()
cinema.entry_hall(5, 5, 11)
print(cinema.hall_list[0].show_list)
for hall in cinema.hall_list:
    print(hall.rows, hall.cols , hall.hall_no)