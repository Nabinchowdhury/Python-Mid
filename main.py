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
        arr = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.seats[id] = arr

    def __handle_seat_booking__(self, id):
        seats_needed = int(input('How many seats?: '))
        if seats_needed < 1:
            print("Please, enter a valid number")
            return self.__handle_seat_booking__(id)
        else:
            tuple_list_input = input("Enter a list of tuples (e.g., (1,2) (3,4) (5,6)): ")
            tuple_list_input = tuple_list_input.replace('(', '').replace(')', '')
            tuple_list = []
            try:
                # print(type(tuple(tuple_list_input)))
                # if type(tuple_list_input) is not tuple:
                #     print('not as example. please add command as shown')
                #     return self.__handle_seat_booking__(id)
                tuple_strings = tuple_list_input.split()
                tuple_list = [tuple(map(int, tup.split(','))) for tup in tuple_strings][0:seats_needed]
                for i in tuple_list:
                    self.seat_booked.append(i)
                    if self.seats[id][i[0]-1][i[1]-1] == 1:
                        print('this seat is already booked. Please try some other seat')
                        return self.__handle_seat_booking__(id)
                    # self.seat_booked.append()
                    # if row < 1 or row > self.rows:
                    #     print("Please, enter a valid number")
                    #     self.__handle_seat_booking__(id)
                    # col = int(input(f'Which column for seat {i+1}?: '))
                    # if col < 1 or col > self.cols:
                    #     print("Please, enter a valid number")
                    #     self.__handle_seat_booking__(id)

                    self.seats[id][i[0]-1][i[1]-1] = 1
                print('Booking successful! seat no', self.seat_booked)
                init_counter()
            except:
                print('invalid seat info. please add command as shown')
                self.__handle_seat_booking__(id)
         
    def __book_seats__(self, id):
        selected_show = ''
        for show in self.show_list:
            if show[0] == id:
                selected_show = show
        
        if not selected_show:
            print('Invalid show id. please add a valid show id')
            book_shows()
        else:
            self.__handle_seat_booking__(id)
        
    def __view_available_seats__(self, id):
        if id not in self.seats:
            print('please add a valid id')
            return checkAvailableSeats()
        for seats in self.seats[id]:
            print(seats)

    def __view_show_list__(self):
        print('hall no : ', self.hall_no, ', Shows available: ', self.show_list)

class Star_Cinema(Hall):
    hall_list = []
    def __init__(self) -> None:
        pass

    def __entry_hall__(self, rows, cols, hall_no):
        super().__init__(rows, cols, hall_no)
        self.hall_list.append(self)

def book_shows():
    id = str(input('Enter show ID: '))
    cinema.hall_list[0].__book_seats__(id)

def checkAvailableSeats():
    id = str(input('Enter show iD to see seats : '))
    cinema.__view_available_seats__(id)

def viewAvailableShows():
    for hall in cinema.hall_list:
        hall.__view_show_list__()
    print('To book show, enter 1')
    print('To see available seats, enter 2')
    print('Go back to initial page, enter 0')
    inp = str(input('Enter number here : '))
    if inp == '0':
        init_counter()
    elif inp == '1':
        book_shows()
    elif inp == '2':
        checkAvailableSeats()
    else: 
        print('Please add valid number')
        viewAvailableShows()
        
#***************adding new shows*******************
def input_show_entry(id = '', name = '', time = ''):
    id = id or str(input('Enter show ID to add show: '))
    name =  name or str(input('Enter show name: '))
    time = time or str(input('Enter show time: '))
    cinema.hall_list[0].__entry_show__(id, name, time)
    init_counter()

def add_hall():
    rows = int(input('add hall rows: '))
    cols = int(input('add hall cols: '))
    id = int(input('add hall id: '))
    cinema.__entry_hall__(rows, cols, id)

def init_counter():
    print('To see available shows, enter 1')
    print('To add new hall , enter 2')
    inp = int(input('Add number here : '))
    if inp == 1:
        viewAvailableShows()
    elif inp == 2:
        input_show_entry()    

cinema = Star_Cinema()
cinema.__entry_hall__(5, 5, 11)
input_show_entry('111', 'Moana_2', '4pm')
init_counter()