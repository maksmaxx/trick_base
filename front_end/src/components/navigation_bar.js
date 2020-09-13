import React, { Component } from "react";
import { Navbar } from "react-bootstrap";
import { connect } from "react-redux";
import Logo from '../assets/logo.png'; 
import { updateActivePage } from "../store/actions/actions";

class NavigationBar extends Component {
    handleClick = () => {
        this.props.updateActivePage("HOME_PAGE");
    }

    render() {
        return (
            <Navbar variant="dark" sticky="top">
            <div className="transparent-button" onClick={this.handleClick}>
                <Navbar.Brand>
                    <img
                        src={Logo}
                        width="65"
                        height="65"
                        className="d-inline-block"
                        alt="Logo"
                    />
                    <p className="d-inline-block trick">Trick</p>
                    <p className="d-inline-block base">Base</p>
                </Navbar.Brand>
            </div>
        </Navbar>
    );
    }
}

const mapDispatchToProps = (dispatch) => {
    return {
        updateActivePage: (page) => { dispatch(updateActivePage(page)) }
    }
}

export default connect(null, mapDispatchToProps)(NavigationBar);