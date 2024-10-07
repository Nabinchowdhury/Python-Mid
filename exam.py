class Hall:
    def __init__(self, rows, cols, hall_no) -> None:
        self.seats = {}
        self.seat_booked = []
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no

    def __entry_show__(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self.show_list.append(show_info)
        arr = [[0]*self.cols] * self.rows
        self.seats[id] = arr

    def handle_seat_booking(self, id):
        seats_needed = int(input('How many seats?: '))
        if seats_needed < 1:
            print("Please, enter a valid number")
            return self.handle_seat_booking(id)
        else:
            for i in range(seats_needed):
                row = int(input(f'Which row for seat {i+1}?: '))
                if row < 1 or row > self.rows:
                    print("Please, enter a valid number")
                    self.handle_seat_booking(id)
                col = int(input(f'Which column for seat {i+1}?: '))
                if col < 1 or col > self.cols:
                    print("Please, enter a valid number")
                    self.handle_seat_booking(id)

                self.seat_booked.append((row-1, col-1))
                self.seats[id][col-1][row-1] = 1
            print(self.seat_booked, self.seats[id])
    def __book_seats__(self, id):
        selected_show = ''
        for show in self.show_list:
            if show[0] == id:
                selected_show = show
        
        if not selected_show:
            print('Invalid show id. please add a valid show id')
            book_shows()
        else:
            print(show)
            self.handle_seat_booking(id)

class Star_Cinema(Hall):
    hall_list = []
    def __init__(self) -> None:
        pass

    def __entry_hall__(self, rows, cols, hall_no):
        super().__init__(rows, cols, hall_no)
        self.hall_list.append(self)

cinema = Star_Cinema()
cinema.__entry_hall__(2, 5, 11)

def book_shows():
    id = str(input('Enter show ID: '))
    cinema.hall_list[0].__book_seats__(id)

def input_show_entry():
    id = str(input('Enter show ID: '))
    name = str(input('Enter show name: '))
    time = str(input('Enter show time: '))
    cinema.hall_list[0].__entry_show__(id, name, time)
    for hall in cinema.hall_list:
        print(hall.seats)
        # print(hall.show_list, hall.rows, hall.cols)
        # hall.
        # print(hall.show_list[id])
        # for show in hal.
# for hall in cinema.hall_list:
#     print(hall.rows, hall.cols , hall.hall_no, hall.show_list)

input_show_entry()
book_shows()
# input_show_entry()
