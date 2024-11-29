const express = require("express");

const app = express();

const PORT = 8080;

app.set("view engine", "html");

//* TXT
app.get("/txt", (req, res) => {
  res.status(200).send("Hi");
});

//* HTML
app.get("/html", (req, res) => {
  res.render("./index");
});

//* JSON
app.get("/json", (req, res) => {
  res.status(200).json({
    name: "Lucas",
    lastName: "Valdez",
    likes: ["icecream", "reading", "music"],
    dislikes: ["fish", "cigarettes"],
  });
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
