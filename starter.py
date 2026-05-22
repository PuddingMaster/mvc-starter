import uuid
class User:
    """A user"""

    def __init__(self, user_id: str, name: str):
        """
            Initialize a new user

            Parameters:

                user_id: the user's id

                name: the user's name
        """

        self._id = user_id
        self._name = name
    
    def get_name(self) -> str:
        """
            Returns the user's name.
        """
        return self._name
    
    def get_user_id(self) -> str:
        """
            Returns the user's id.
        """
        return self._id
    
    def __repr__(self) -> str:
        """
            Returns a full representation of the user.
        """

        return f"{self.__class__.__name__}('{self._id}', '{self._name}')"
    
    def __eq__(self, other: User) -> bool:
        """
            Returns True if this user is equal to the other user.
        """

        return self._id == other.get_user_id()

class Student(User):
    """A student"""
    def enroll(self, ticket_id: str) -> str:
        return f"{self._name} (Student) enrolled ticket {ticket_id}"

class Staff(User):
    """A Staff Member"""
    def report(self, ticket_id: str) -> str:
        return f"{self._name} (Staff) reported ticket {ticket_id}"
    
class TA(Student, Staff):
    """A Teaching Assistant (Assistent?)"""

    def __init__(self, user_id: str, name: str, 
                 level: str, school: str):
        """
            Initialize a new TA

            Parameters:

                user_id: the TA's id

                name: the TA's name

                level: the TA's level

                school: the TA's school
        """
        super().__init__(user_id, name)
        self._level = level
        self._school = school
    
    def assist(self, ticket_id: str) -> str:
        return f"{self._name} (TA) handling ticket {ticket_id}"
    
    def __repr__(self) -> str:
        """
            Returns a full representation of the user.
        """

        return (f"TA('{self._id}', '{self._name}', "
                f"'{self._level}', '{self._school}')")


class Comment:
    """A comment written by user"""
    def __init__(self, author: User, text: str):
        self._author = author
        self._text = text
    
    def get_author(self) -> User:
        return self._author
    
    def get_text(self) -> str:
        return self._text
    
    def __repr__(self) -> str:
        return f"Comment({repr(self._author)}, '{self._text}')"


class Ticket:
    """A ticket opened by a user"""
    def __init__(self, ticket_id: str, subject: str, 
                 opened_by: User, status = "Open"):
        self._ticket_id = ticket_id
        self._subject = subject
        self._opened_by = opened_by
        self._status = status
        self._comments = []
    
    def __repr__(self) -> str:
        return (f"Ticket({self._ticket_id}, {self._subject}, "
                f"{self._opened_by}, {self._status})")

    def get_ticket_id(self) -> str:
        return self._ticket_id
    
    def get_comments(self) -> list[Comment]:
        return self._comments
    
    def set_comments(self, comments: list[Comment]) -> None:
        self._comments = comments

    def add_comment(self, comment: Comment) -> None:
        self._comments.append(comment)

    def change_status(self, status: str) -> None:
        if type(status) == type(''):    
            self._status = status
        else:
            raise TypeError("Status must be str")


class TAQueue:
    """A queue of tickets for TAs"""
    def __init__(self, tickets: list[Ticket] = []):
        self._tickets = tickets

    def get_tickets(self):
        return self._tickets

    def enqueue(self, ticket: Ticket) -> None:
        self._tickets.append(ticket)

    def dequeue(self) -> Ticket | None:
        if self._tickets:
            return self._tickets.pop(0)
    
    def peek(self) -> Ticket | None:
        if self._tickets:
            return self._tickets[0]
    
    def __repr__(self) -> str:
        return f"TAQueue({len(self._tickets)} tickets)"

class ConsoleView:

    def show_ticket(self, ticket: Ticket) -> None:
        print(f" - {repr(ticket)}")

    def show_queue(self, queue: TAQueue) -> None:
        print(repr(queue))


class HelpCentreController:

    def __init__(self, queue: TAQueue, view: ConsoleView):
        self._queue = queue
        self._view = view
        self._current = []

    def submit_ticket(self, tid: str, subject: str, user: User) -> Ticket:
        ticket = Ticket(tid, subject, user)
        self._queue.enqueue(ticket)
        return ticket
    
    def assign_next(self, ta: TA) -> None:
        if self._queue.peek():
            self._current.append(ta.assist(self._queue.peek().get_ticket_id()))
            self._queue.dequeue()

    def print_queue(self) -> None:
        if self._current:
            for currently_handling in self._current:
                print(currently_handling)
        self._view.show_queue(self._queue)
        for ticket in self._queue.get_tickets():
            self._view.show_ticket(ticket)