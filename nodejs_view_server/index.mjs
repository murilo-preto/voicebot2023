import express from "express";
import axios from "axios";
import jwt from "jsonwebtoken";

const app = express();
const port = process.env.PORT || 3000;

app.set("view engine", "ejs");
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

const secretKey = 'your-secret-key';
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

// Example: Protecting a route using the middleware
app.get('/protected-route', authenticateJWT, (req, res) => {
  res.send(`Welcome, ${req.user.username}!`);
});

app.get("/", function (req, res) {
  res.render("pages/index");
});

app.get("/login", function (req, res) {
  res.render("pages/login");
});

app.post("/login", async (req, res) => {
  console.log('Received POST request:', req.body);

  // const username = req.body.uname;
  // const password = req.body.psw;

  const url = 'http://127.0.0.1:5000/api/login';
  const postData = {
    uname: req.body.uname,
    psw: req.body.psw,
  };

  axios.post(url, postData)
  .then(response => {
    // Handle the successful response
    console.log('Response:', response.data);

    if (response==401){
      res.status(401).send("Invalid credentials");
    }
    else{
      res.status(200).send("Login sucessfull");
    }
  })
  .catch(error => {
    // Handle errors
    console.error('Error:', error.message);
  });
});

app.listen(port, () => {
  console.log(`Ouvindo na porta ${port}`);
});
