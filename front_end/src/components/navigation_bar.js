import React from "react";
import { Navbar } from "react-bootstrap";
import { Link } from "react-router-dom";
import Logo from '../assets/logo.png'; 

const NavigationBar = () => {
    return (
        <Navbar variant="dark" sticky="top">
            <Link to="/">
                <Navbar.Brand>
                    <img
                        src={Logo}
                        width="65"
                        height="65"
                        className="d-inline-block"
                        alt="Logo"
                    />
                    <p className="d-inline-block trick">
                        Trick
                    </p>
                    <p className="d-inline-block base">
                        Base
                    </p>
                </Navbar.Brand>
            </Link>
        </Navbar>
    );
}

export default NavigationBar;