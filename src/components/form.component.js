import React, { useState } from "react";
import {Text} from "react-native";

const Form = ({ handleSubmit, history }) => {
    const [searchEntry, setSearchEntry] = useState("");

    const updateSearchInput = e => {
        setSearchEntry(e.target.value);
    };

    return (
        <form
            className="search-form"
            onSubmit={e => handleSubmit(e, history, searchEntry)}
        >
            <input 
                type="text"
                name="search"
                placeholder="Enter a YouTube URL..."
                onChange={updateSearchInput}
                value={searchEntry}
            />
            <button
                type="submit"
                className={`search-button ${searchEntry.trim() ? "active" : null}`}
                disabled={!searchEntry.trim()}
            ><Text style={{color: '#000000'}}>Find Similar Songs</Text></button>
        </form>
    );
};

export default Form;