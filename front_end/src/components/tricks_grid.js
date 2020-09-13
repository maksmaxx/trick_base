import React, { Component } from "react";
import { Container, Spinner } from "react-bootstrap";
import { connect } from "react-redux";
import { Link } from "react-router-dom";

class TricksGrid extends Component  {
    generateTricks = () => {
        // Generate grid of existing disciplines basing on activeDiscipline stired in Redux
        const items = this.props.activeTricks ? this.props.activeTricks.map(item => {
            return (
                <Link to={"/tricks/" + item.uuid} key={item.name}>
                    <div>{item.name}</div>
                </Link>
            )
        }) : null;

        return items;
    }
    render() {
        const tricks = this.generateTricks();
        const view = tricks ? (
            <div className="grid">
                { tricks }
            </div>
        ) : (
            <Spinner className="center" animation="border" role="status">
                <span className="sr-only">Loading...</span>
            </Spinner>
        );
        return (
            <Container>
                { view }
            </Container>
        );
    }
}

const mapStateToProps = (state) => {
    // Get state from Redux and pass to component's props
    return {
        activeTricks: state.activeTricks,
    }
}

export default connect(mapStateToProps)(TricksGrid);