import React from "react";
import Form from "./form.component";
import {Text} from "react-native";

const Header = ({ history, handleSubmit }) => {
    const styleObj = {
        fontSize: 60,
        color: "white",
        }
    return (
        <div>
            <h1 style = {styleObj}>Song Explore</h1>
            <Form history={history} handleSubmit={handleSubmit} />
        </div>
    );
};

export default Header;