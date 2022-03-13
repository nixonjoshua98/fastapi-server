Server written in FastAPI for a game I was developing. Pulled into a public repository.

- Uses a 'handler' approach inspired by the mediator pattern to seperate logic from the endpoints
- Uses FastAPI to inject Services, Repositories (should have further split out into a service for each repo), Handlers