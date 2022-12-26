const express = require("express");
const { spawn } = require("child_process");

class BusArrivalAPI {
  constructor() {
    this.app = express();
    this.setupRoutes();
  }

  setupRoutes() {
    this.app.get("/arrival-times/:busStopCode/:busNumber", (req, res) => {
      this.handleArrivalTimesRequest(req, res);
    });
  }

  handleArrivalTimesRequest(req, res) {
    const { busStopCode, busNumber } = req.params;
    const pythonScript = spawn("python", ["path/to/BusArrivalAPI.py", busStopCode, busNumber]);

    let arrivalData = "";

    pythonScript.stdout.on("data", data => {
      arrivalData += data;
    });

    pythonScript.stderr.on("data", data => {
      console.error(`Received error from Python script: ${data}`);
    });

    pythonScript.on("close", code => {
      if (code === 0) {
        res.send(arrivalData);
      } else {
        res.status(500).send("An error occurred while calling the Python script.");
      }
    });
  }

  start() {
    this.app.listen(3000, () => {
      console.log("API listening on port 3000");
    });
  }
}

const api = new BusArrivalAPI();
api.start();
