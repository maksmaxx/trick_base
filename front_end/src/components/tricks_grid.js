import React, { Component } from "react";
import { Card, Container, Spinner} from "react-bootstrap";
import { connect } from "react-redux";
import { Link } from "react-router-dom";

class TricksGrid extends Component  {
    generateTricks = () => {
        // Generate grid of existing disciplines basing on activeDiscipline stired in Redux
        const items = this.props.activeTricks ? this.props.activeTricks.sort().map(item => {
            const name = item.name.charAt(0).toUpperCase() + item.name.slice(1);

            return (
                <Link to={"/tricks/" + item.uuid} key={item.name}>
                    <Card className="card">
                        <Container className="card-body align-items-center d-flex justify-content-center">
                            <h4 className="card-title">{name}</h4>
                        </Container>
                    </Card>
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