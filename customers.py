"""Customers at Hackbright."""


class Customer:
    """Ubermelon customer."""

    # TODO: need to implement this

    def __init__(self,
        customer_first,
        customer_lastname,
        email,
        secret
    ):

         self.customer_first=customer_first
         self.customer_lastname=customer_lastname
         self. email=email
         self.secret=secret
        # pass


def __repr__(self):
        """Convenience method to show information about melon in console."""

        return (
            f"<Melon: {self.customer_first}, {self.customer_lastname}, {self.email}, {self.secret}>"
        )

        def read_customer_from_file(filepath):

            customer_info = {}
        
        with open(filepath) as file: 
            for line in line:
                ( customer_first,
                  customer_lastname,
                  email,
                  secret
                ) = line.strip.split('|')

                customer_info[email] = customer(
                  customer_first,
                  customer_lastname,
                  email,
                  secret
                )

        return customer_info

def get_by_emai(email):


    return customer_info[email]

customer_info = read_customer_from_file('customers.txt')

        