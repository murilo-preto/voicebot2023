import express from "express";
import jwt from "jsonwebtoken";
import cors from 'cors';

const app = express();
const port = process.env.PORT || 3000;
const secretKey = '12345';

// Middleware to enable Cross-Origin Resource Sharing (CORS)
app.use(cors());

// Set the view engine and configure middleware for parsing requests
app.set("view engine", "ejs");
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(express.static('public'))

// Middleware to authenticate JWT
const authenticateJWT = (req, res, next) => {
  const tokenHeader = req.header('Authorization');

  if (!tokenHeader) {
    return res.status(401).send('Unauthorized. Please provide a valid token.');
  }

  const token = tokenHeader.split(' ')[1]; // Assuming the format is 'Bearer <token>'

  jwt.verify(token, secretKey, { algorithms: ['HS256'] }, (err, user) => {
    if (err) {
      console.error(err);
      return res.status(403).send('Token verification failed.');
    }

    req.user = user;
    next();
  });
};

// Define routes
app.get("/", (req, res) => {
  res.render("pages/index");
});

app.get("/login", (req, res) => {
  res.render("pages/login");
});

app.get("/voicebot", authenticateJWT, (req, res) => {
  res.render("pages/voicebot");
});

app.get("/chatbot", authenticateJWT, (req, res) => {
  res.render("pages/chatbot");
});

app.get('/favicon.ico', (req, res) => {
  res.status(204).end();
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
