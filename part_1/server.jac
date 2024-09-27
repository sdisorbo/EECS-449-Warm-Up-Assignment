walker interact {
    can return_message with entry {
        report {
            "response": "Hello, world!"
        };
    }
}

walker interact_with_body {
    has name: str;

    can return_message with entry {
        report {
            "response": "Hello, " + self.name + "!"
        };
    }
}

walker interact_with_body_and_query {
    has name: str;
    has age: int;

    can return_message with entry {
        report {
            "response": "Hello, " + self.name + "! You are " + str(self.age) + " years old."
        };
    }
}

walker add_numbers {
    has num1: int;
    has num2: int;

    can return_message with entry {
        report {
            "response": "The sum is: " + str(self.num1 + self.num2)
        };
    }
}
