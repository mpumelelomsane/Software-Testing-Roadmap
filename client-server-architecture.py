#CLIENT-SERVER ARCHITECTURE
"""It's all starts with the appplication , lets say we want to create a calculator 
program that accepts user inputs and perfom desired operations on the input. A programmer 
 then creates an application and release it as a library. To use it, everyone have to dowload
 this library and then use it in their project. Over time, this library gets famous and 
 a non-technical user wants to use it. The management team asks the programmer who inveted this 
 library to create a WEB APPLICATION and its WEB API since the programmer knows 
 all these technologies.
 A programmer then starts creating a web application and DEPLOY it in a WEB SERVER so that
 this application will be available as a WEB SERVICE. """

 ## The SERVER in which the application are deployed are generally known as APPLICATION SERVERS
 ## The Application that is running on the server is known as a WEB SERVICE. 
 #(as it provides the service of a web)
 ## The consumer who uses/consumes the service is called a CLIENT 

 """The CLIENT communicates over the SERVER via the HTTP methods and receives the response. 
 During communication the client sends a request in a predefined format and also receives 
 the response in the same format. """

 """The SERVER exposes APIs in a specific format, and the client is only authorised
 to call the exposed APIs. In API call we use a particular logic which is wrapped inside 
 the format of API. The Client passes the arguments and the Server does all the calculations."""

 """The DATA FORMAT which moves from client to server and vice versa can be in any specific
 format.(XML, JSON, TEXT, FILE)- In this way we are using functionality of a software over
 the web."""

 ##SUMMARY 
 """CLIENT uses an API to send a request over the network. Once the server receives 
 the call it processes all the data and gives the feedback /response to the client.
 In this way the SERVER can provide services to multiple clients at the same time."""