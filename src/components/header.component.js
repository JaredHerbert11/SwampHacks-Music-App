import React from "react";
import Form from "./form.component";

const Header = ({ history, handleSubmit }) => {
    return (
        <div>
            <h1>Song Explore</h1>
            <Form history={history} handleSubmit={handleSubmit} />
        </div>
    );
};

export default Header;