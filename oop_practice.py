"""
This is a Classes and OOP tutorial, guided by PythonGuides.com examples have been changed by me to create some uniqueness

To make this a little realer than just creating a simple object we'll try to create something more applicable to what you'll
actually be working on as a software engineer.

Problem:
- Create an object to represent a payload receieved from an external API
- Take in a payload as JSON (coming from a make believe API)and give our payload object the data in the payload
Lets say we contracted an AI company that says they can take our customer analytics and return a response payload of metrics the user should do
So we'll have two classes
1. Payload we send to contractor
2. Payload we receive from contractor(in real life you wouldn't write this but we're doing it for practice so shape up)

2nd object
- Time they should post to social media
- platform their niche is best in

What is Object Orient Programming(OOP)?
- It is a programming paradigm that organizes code around the concept of "objects", it allows us to create reusable and maintainable code while also
allowing us to work with other developers.

"""

# To create a class, you use the "class" keyword.
class MVAIPayload:
    def __init__(self, company_type, total_viewers, peak_posting_time):
        self.company_type = company_type
        self.total_viewers = total_viewers
        self.peak_posting_time = peak_posting_time

# __init__ is a special method called a constructor, it CONSTRUCTS the new object with the values we give it, see line 38
    
    # __str__ is a common function, it is used to represent the object as a string
    def __str__(self):
        return f"Company info {self.company_type} {self.total_viewers} {self.peak_posting_time}"
    

# Creating an Instance
company1 = MVAIPayload("manufacturing", 100000, "2:00") # this is how you create an instance of a class
print(company1.__str__()) # this is how you print the contents of an object

"""
Lets make believe the payload they send back comes through something like Kafka and it's a JSON

payload = {
    time_to_post: "3pm",
    platform_to_post_to: "YouTube"
}

Now we want to create some code that parses through this payload 

for key, value in payload.items():
    print(value)

TO BE CONTINUED

"""

for key, value in payload.items():
    print(value)