import React, { useState, useEffect } from 'react';
import axios from "axios";

const ResultsPage = ({searchTerm}) => {
    let cartItems = [];
    let [recs, setRecs] = useState([]);
    const styleObj = {
        fontSize: 50,
        color: "white",
        }

    return (
        <h1 style = {styleObj}>Matching Songs</h1>

    )
}

export default ResultsPage;