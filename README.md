Task Description:

Build a containerized application with three services: frontend (React), backend (FastAPI), and database (SQLite). The application should run with a single command (docker-compose up) and be accessible at http://localhost:1234. The application consists of:

Frontend (React):
Display a list of book titles fetched from the backend.
If the backend service is unavailable, display an error message.

Backend (FastAPI):
Provides a RESTful API with the following endpoints:
GET /books: Fetch a list of books.
GET /books/{id}: Get a specific book by ID.
POST /books: Create a new book.
PUT /books/{id}: Update a book's title by ID.
DELETE /books/{id}: Delete a book by ID.
Use SQLAlchemy for database interaction with SQLite.
Seed the database with some books on startup.

Database (SQLite):
Store books with two fields: id and title.

Docker:
Use Docker Compose to orchestrate the three services, ensuring communication between frontend, backend, and database.
Gracefully stop services when running docker-compose down.

Steps:
1. Clone the Repository
    If you haven't already, clone the codebase to your local machine:

   	git clone https://github.com/sweedanoronha/bookstore_app.git
   	Change into the project directory:
    cd your-repo-name

3. Set Up the Backend (FastAPI)
    Open the Project in VS Code:
    
    Open VS Code and then open the folder where your project is located.
    Create and Activate a Virtual Environment:
    
    Open the integrated terminal in VS Code (`Ctrl + `` or through the menu: View > Terminal).
    Create a virtual environment:
    python -m venv venv
    
    Activate the virtual environment:
    
    On Windows:
    venv\Scripts\activate
    On macOS/Linux:
    source venv/bin/activate
    
    Install Dependencies:
    
    Make sure you have a requirements.txt file with the necessary packages. If you don’t have one, create it in the backend folder with the following content:
    plaintext
    Copy code
    fastapi==0.95.1
    uvicorn==0.22.0
    sqlalchemy==1.4.32
    pydantic==1.10.2
    Install the packages using:
    
    pip install -r requirements.txt
    Run the FastAPI Backend:
    
    You can run the FastAPI app using Uvicorn. In the terminal, navigate to the folder where your main FastAPI application file is located (usually backend/app or similar).
    Run the server:
    
    uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
    This command will start the FastAPI application, and you can access it at http://localhost:8000.
    
    Verify API Access:
    
    Open a web browser and navigate to http://localhost:8000/docs to access the auto-generated API documentation provided by FastAPI.

4. Set Up the Frontend (React)
		Create React App:
		
		In the terminal, navigate to the folder where you want to create the React app (usually at the root of your project).
		
		npx create-react-app frontend
		Navigate to the Frontend Directory:
		
		Change to the frontend directory:
		
		cd frontend
		
		Install Axios (for API calls):
		
		Install Axios to make HTTP requests to the FastAPI backend:
		npm install axios
		
		Run the React App:
		
		Still in the frontend directory, start the React application:
		npm start
		This command will start the React app and should automatically open http://localhost:123 in your web browser.

4. Running Everything Together
		Make sure both the FastAPI backend and the React frontend are running:
		
		FastAPI should be accessible at http://localhost:8000.
		React should be accessible at http://localhost:1234.
		Your React app should now display the list of books fetched from the FastAPI backend.

5. Using Docker 
		If you prefer to use Docker for both the frontend and backend:
		
		Then, run:
		
		docker-compose up
		This command will build the services and run them in Docker containers.

6. Testing
		To test the setup, navigate to http://localhost:1234 in your browser. You should see the book list fetched from the FastAPI backend.
		If the backend is stopped, the frontend should display an appropriate message.
