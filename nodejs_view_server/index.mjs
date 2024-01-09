import express from 'express';

const app = express()
const port = process.env.PORT || 3000;

app.set("view engine", "ejs");
app.use(express.json());

app.get("/", function (req, res) {
    res.render("pages/index");
  });

  app.get("/login", function (req, res) {
    res.render("pages/login");
  });

app.listen(port, () => {
  console.log(`Ouvindo na porta ${port}`)
})