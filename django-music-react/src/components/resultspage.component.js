import React, { useState, useEffect } from 'react';
import axios from "axios";

const ResultsPage = ({searchTerm}) => {
    let cartItems = [];
    let [recs, setRecs] = useState([]);

    return (
        <h1>Results for {searchTerm}</h1>

    )
}

export default ResultsPage;