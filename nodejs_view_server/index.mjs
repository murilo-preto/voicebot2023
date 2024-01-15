import express from "express";
import axios from "axios";
import jwt from "jsonwebtoken";
import cors from 'cors';

const app = express();
const port = process.env.PORT || 3000;

app.use(cors());
app.set("view engine", "ejs");
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

const secretKey = 'your-secret-key';

// Middleware to authenticate JWT
const authenticateJWT = (req, res, next) => {
  const token = req.header('Authorization');

  if (!token) {
    return res.status(401).send('Unauthorized. Please provide a valid token.');
  }

  jwt.verify(token, secretKey, (err, user) => {
    if (err) {
      return res.status(403).send('Token verification failed.');
    }

    req.user = user;
    next();
  });
};

// Homepage route
app.get("/", (req, res) => {
  res.render("pages/index");
});

// Login page route
app.get("/login", (req, res) => {
  res.render("pages/login");
});

// Login route handling
app.post("/login", async (req, res) => {
  try {
    const { uname, psw } = req.body;
    const postData = { uname, psw };

    // console.log(req.body.uname);
    // const postData = req.body;
    const url = 'http://127.0.0.1:5000/api/login';

    // Making axios request to external API for login
    const response = await axios.post(url, postData);

    // Check for invalid credentials
    if (response.status === 401) {
      return res.status(401).send("Invalid credentials");
    }

    // Extracting access token from the response and sending it in the JSON response
    const accessToken = response.data.access_token;
    res.json({ access_token: accessToken });
  } catch (error) {
    // Handling unexpected errors
    console.error('Error:', error.message);
    res.status(500).send('Internal Server Error');
  }
});

// Protected route requiring JWT authentication
app.get('/protected-route', authenticateJWT, (req, res) => {
  res.send(`Welcome, ${req.user.username}!`);
});

// Server listening on specified port
app.listen(port, () => {
  console.log(`Listening on port ${port}`);
});
