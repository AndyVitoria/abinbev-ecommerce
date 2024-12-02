First I started with the idea of modeling the problem using UML.
I created a class diagram to represent the entities and their relationships such as the one below:

![Class Diagram](docs/images/image-2.png)

Soon I noticed this approach was not the best for this project, due to the deadline and available time, so I decided to implement starting from the routes and the use cases.

I created the routes, use cases, and entities for the Users, unifying the Admin and Clients in the same entity.
The only difference between them is the role.


I wrote the unit test for the entities and routes and then, I noticed again, that delivering the project with the tests was not the best approach, so I decided to remove the tests and focus on the implementation.

For the test, my main idea was to show how I structure my projects. Usually, I rather do the type checking in the Entities, and write test cases for different types to get common bugs related to the data types.

Then I write for each new class, a test case to check the class' behavior, mocking the dependencies to isolate the class from external variables.

When I noticed that with my current speed, I was not going to be able to deliver the project with the tests, I decided to focus on the functionalities' development and discuss the tests in the interview.

## Implementation

The approach that I selected was to start implementing the routes and entities, mapping the necessity of the use cases, and making an initial draft of it. Then, only when I began to implement the use case that I write the repositories models.

To handle the communication with the database, I've implemented the SQLLiteInterface class, a simple class responsible for creating an interface for the database with the CRUD operations.

For this project, I've selected SQLModel as an ORM to handle the database models, because it is a simple and easy-to-use ORM. A friend of mine suggested it once in a project and because of it is compatible with FastAPI.

I did a quick search to understand how to use the ORM, but after that, I got ready to implement the models and the repositories without any problem.

## Challenges

The main challenge was to implement the authentication and authorization for the routes.
I've never implemented this kind of feature before, so I needed to do a quick search to understand how to implement it.

I discovered that FastAPI has a built-in feature to manage authentication and authorization, so, I decided to use it.
I isolated the responsibility of the authentication and authorization in the LoginUseCase, to facilitate the maintenance.

I also used the PyJWT to delegate the token generation and validation.

Another challenge was to develop this whole project without the tests.

I'm used to writing unit tests for my projects. And with more time I would be able to deliver the project with a better test coverage, but for a technical test, I think that I can express myself better enough in the report and the interview.

## Conclusion

I'm happy with the result of the project, I was able to implement the main functionalities and the authentication and authorization for the routes. It was fun to implement this project, I refreshed some concepts that I was not using for a while, and also learned about SQLModel and Authentication, even if it was a simple implementation.

I'm looking forward to the feedback, and I'm available for any questions.
