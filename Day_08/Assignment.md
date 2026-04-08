Q1: What is a list in Python, and how is it used in DevOps?
ans: list is the data structure used for storing list of items. datatypes of the storing elements can be different. it is mutable.
it is used when we need to store the server names currently being used by the  application.


Q2: How do you create a list in Python, and can you provide an example related to DevOps?
by using square brackets.
eg: my_list=["A",1,"B",1.5,"C"]
eg:my_server=["web-server_1","web-server_2","webserver_3"]


Q3: What is the difference between a list and a tuple in Python, and when would you choose one over the other in a DevOps context?
(a) list is mutable
tuple is immutable
(b) syntactically: list represented by square brackets : []
tuple by parenthesis : ()
(c) performance: list is comparatively slower than tuple because list is mutable so needs realloctaion during modifying the list
tuple is faster than list because it is immutable so reallocation of memory does not happen in this
(d) usage: list is used where updation, adding, removing element is required , eg: currently server names are in use on my application/machine
tuple is used where modification is not safe, eg: tuple for names of administrative users 


Q4: How can you access elements in a list, and provide a DevOps-related example?
by index.
eg:my_server=["web-server_1","web-server_2","webserver_3"], do first_element=my_server[0].
it will give the first element and so on.


Q5: How do you add an element to the end of a list in Python? Provide a DevOps example.
using append inbuilt function : my_server.append()
eg:my_server=["web-server_1","web-server_2","webserver_3"]
my_server.append("web-server_4")


Q6: How can you remove an element from a list in Python, and can you provide a DevOps use case?
using remove inbuilt function: my_server.remove()
eg:my_server=["web-server_1","web-server_2","webserver_3"]
my_server.append("web-server_3")
