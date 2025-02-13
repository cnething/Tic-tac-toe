const express = require('express');
const cors = require('cors');
const app = express();
const mysql = require('mysql')
app.use(cors())
app.get('/', (req, res) => res.send('Backend is running!'));
app.use(express.json());

const conDibbs = mysql.createPool({
    host:"localhost",
    user:"root",
    password:"Cp020898",
    database:"Project2"
})

const PORT = process.env.PORT || 8000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
//get total bill

app.post('/totalbill', (req, res) => {
    const { totalBill, tipPercent, tipAmount, totalAmount } = req.body;

    if (!totalBill || !tipPercent || !tipAmount || !totalAmount) {
        return res.status(400).json({ status: "error", message: "Missing required fields" });
    }

    const strCommand = `INSERT INTO tblTip (totalBill, tipPercent, tipAmount, totalAmount) VALUES (?, ?, ?, ?)`;

    conDibbs.query(strCommand, [totalBill, tipPercent, tipAmount, totalAmount], (error, results) => {
        if (error) {
            console.error("Query execution error:", error);
            return res.status(500).json({ status: "error", message: "Query execution error" });
        }

        res.status(201).json({ status: "success", message: "Bill inserted successfully", data: results });
    });
});