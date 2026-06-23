# Exercise: Design Pattern Implementation Challenge

## Factory Pattern Opportunity (Python)

**Document the benefits gained from the Factory Method pattern implementation**

- The design pattern I went for was the Factory Method style due to the code having multiple product type that will be traded off with for more classes.

- Firstly, it removed the big conditional before `connect()` had an if statement that checked different database type, now factory chooses the correct class so `connect()` no longer needs to know every database type.

- Before DatabaseConnection did everything now its separated into different classes, `DatabaseConnectionFactory` chooses the correct flow, `DatabaseConnection` handles shared connection flow, `MySQLConnection` handles MySQL logic, `PostgreSQLConnection` handles PostgreSQL logic, `MongoDBConnection` handles MongoDB logic and `RedisConnection` handles Redis logic.

- Other benefit is the ease of adding SQLite or Oracle that meant editing the big `Connect()` method, now can just add a new class and register it in the factory.

- Biggest time saving benefit is when debbuging, meaning you do not need to scan through long conditional just go straight to the class.

- The system is more open to extension and more modifiable as you can just add a new class.

- Because the `DatabaseConnection()` still routes through the factory, existing test and old code will continue to working without having to do a big rewrite.