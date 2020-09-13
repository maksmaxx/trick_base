import React, { Component } from "react";
import { Card, Container, Spinner} from "react-bootstrap";
import { connect } from "react-redux";
import { updateActivePageAndTrick } from "../store/actions/actions";

class TricksGrid extends Component  {
    handleClick = (trick) => {
        this.props.updateActivePageAndTrick("TRICK_PAGE", trick);
    }

    generateTricks = () => {
        // Generate grid of existing disciplines basing on activeDiscipline stired in Redux
        const items = this.props.activeTricks ? this.props.activeTricks
        .sort(function(a, b) {
            // sorts alphabetically
            var textA = a.name.toUpperCase();
            var textB = b.name.toUpperCase();
            return (textA < textB) ? -1 : (textA > textB) ? 1 : 0;
        })
        .map(item => {
            const name = item.name.charAt(0).toUpperCase() + item.name.slice(1);

            return (
                <div>
                    <Card className="card"  key={item.name} onClick={() => this.handleClick(item)}>
                        <Container className="card-body align-items-center d-flex justify-content-center">
                            <h4 className="card-title">{name}</h4>
                        </Container>
                    </Card>
                </div>
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
    return {
        activeTricks: state.activeTricks,
    }
}

const mapDispatchToProps = (dispatch) => {
    return {
        updateActivePageAndTrick: (page, trick) => { dispatch(updateActivePageAndTrick(page, trick)) }
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(TricksGrid);