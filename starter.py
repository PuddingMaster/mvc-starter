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

        return f"User('{self._id}', '{self._name}')"
    
    def __eq__(self, other: User) -> bool:
        """
            Returns True if this user is equal to the other user.
        """

        return self._id == other.get_user_id()

class Student(User):
    """A student"""

    def __init__(self, user_id: str, name: str):
        """
            Initialize a new student

            Parameters:

                user_id: the student's id

                name: the student's name
        """

        super().__init__(user_id, name)
    
    def get_name(self) -> str:
        """
            Returns the student's name.
        """
        return super().get_name()
    
    def get_user_id(self) -> str:
        """
            Returns the student's id.
        """
        return super().get_user_id()
    
    def enroll(self, ticket_id: str) -> str:
        return f"{self._name} (Student) enrolled ticket {ticket_id}"

    def __repr__(self) -> str:
        """
            Returns a full representation of the student.
        """

        return f"Student('{self._id}', '{self._name}')"
    
    def __eq__(self, other: Student | User) -> bool:
        """
            Returns True if this user is equal to the other student.
        """

        return self._id == other.get_user_id()

class Staff(User):
    """A Staff Member"""

    def __init__(self, user_id: str, name: str):
        """
            Initialize a new staff member

            Parameters:

                user_id: the staff's id

                name: the staff's name
        """

        super().__init__(user_id, name)

    def get_name(self) -> str:
        """
            Returns the staff member's name.
        """
        return super().get_name()
    
    def get_user_id(self) -> str:
        """
            Returns the staff member's id.
        """
        return super().get_user_id()
    
    def report(self, ticket_id: str) -> str:
        return f"{self._name} (Staff) reported ticket {ticket_id}"
    
    def __repr__(self) -> str:
        """
            Returns a full representation of the staff member.
        """

        return f"Staff('{self._id}', '{self._name}')"
    
    def __eq__(self, other: Staff | User) -> bool:
        """
            Returns True if this user is equal to the other user.
        """

        return self._id == other.get_user_id()
    
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

        Student.__init__(self, user_id, name)
        Staff.__init__(self, user_id, name)
        self._level = level
        self._school = school

    def get_name(self) -> str:
        """
            Returns the TA's name.
        """
        return super().get_name()
    
    def get_user_id(self) -> str:
        """
            Returns the TA's id.
        """
        return super().get_user_id()
    
    def assist(self, ticket_id: str) -> str:
        return f"{self._name} (TA) handling ticket {ticket_id}"
    
    def __repr__(self) -> str:
        """
            Returns a full representation of the user.
        """

        return (f"TA('{self._id}', '{self._name}', "
                f"'{self._level}', '{self._school}')")
    
    def __eq__(self, other: TA | Student | Staff) -> bool:
        """
            Returns True if this user is equal to the other user.
        """

        return self._id == other.get_user_id()

class Comment:
    
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

    def __init__(self, ticket_id: str, subject: str, 
                 opened_by: User, status: str):
        #TODO: implement
        pass

    def get_ticket_id(self) -> str:
        #TODO: implement
        return ""
    
    def get_comments(self) -> list[Comment]:
        #TODO: implement
        return []
    
    def set_comments(self, comments: list[Comment]) -> None:
        #TODO: implement
        pass

    def add_comment(self, comment: Comment) -> None:
        #TODO: implement
        pass

    def change_status(self, status: str) -> None:
        #TODO: implement
        pass

class TAQueue:

    def __init__(self, tickets: list[Ticket]):
        #TODO: implement
        pass

    def enqueue(self, ticket: Ticket) -> None:
        #TODO: implement
        pass

    def dequeue(self) -> Ticket | None:
        #TODO: implement
        return None
    
    def peek(self) -> Ticket | None:
        #TODO: implement
        return None
    
    def __repr__(self) -> str:
        #TODO: implement
        return ""

class ConsoleView:

    def show_ticket(self, ticket: Ticket) -> None:
        #TODO: implement
        pass

    def show_queue(self, queue: TAQueue) -> None:
        #TODO: implement
        pass

class HelpCentreController:

    def __init__(self, queue: TAQueue, view: ConsoleView):
        #TODO: implement
        pass

    def submit_ticket(self, subject: str, user: User) -> Ticket:
        #TODO: implement
        return None
    
    def assign_next(self, ta: TA) -> None:
        #TODO: implement
        pass

    def print_queue(self) -> None:
        #TODO: implement
        pass