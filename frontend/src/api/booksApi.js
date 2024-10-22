// handles the Axios setup for communicating with the backend.
import axios from 'axios';

// API Base URL: Can be configured in .env file
const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

const booksApi = axios.create({
  baseURL: `${API_BASE_URL}/books`,
});

export default booksApi;
