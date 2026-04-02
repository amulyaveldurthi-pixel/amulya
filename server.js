const express = require("express");
const axios = require("axios");
const cors = require("cors");
require("dotenv").config();

const app = express();
app.use(cors());
app.use(express.json());

app.get("/api/jobs", async (req, res) => {
  const {
    search = "software developer",
    location = "India",
    page = 1,
    jobType,
    minSalary
  } = req.query;

  try {
    const response = await axios.get(
      `https://api.adzuna.com/v1/api/jobs/in/search/${page}`,
      {
        params: {
          app_id: process.env.ADZUNA_APP_ID,
          app_key: process.env.ADZUNA_APP_KEY,
          results_per_page: 10,
          what: search,
          where: location,
          full_time: jobType === "fulltime" ? 1 : undefined,
          part_time: jobType === "parttime" ? 1 : undefined,
          salary_min: minSalary || undefined,
          content_type: "application/json"
        }
      }
    );

    res.json(response.data);
  } catch (error) {
    res.status(500).json({ error: "Error fetching jobs" });
  }
});

app.listen(5000, () => console.log("Server running on port 5000"));