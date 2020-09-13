import React from "react";
import { Navbar, Nav } from "react-bootstrap";

const Footer = () => {
    return (
        <div className="fixed-bottom">  
            <Navbar>
                <Nav className="mx-auto">
                    <Nav.Link href="https://github.com/maksmaxx/trick_base" className="footer-label"> About </Nav.Link>
                </Nav>
            </Navbar>
        </div>
    );
}

export default Footer;