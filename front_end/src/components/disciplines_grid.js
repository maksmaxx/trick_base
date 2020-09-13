import React, { Component } from "react";
import { Container, Card } from "react-bootstrap";
import { connect } from "react-redux";
import {  updateActivePageAndDiscipline } from "../store/actions/actions";

class DisciplinesGrid extends Component  {
    handleClick = (discipline) => {
        this.props.updateActivePageAndDiscipline("DISCIPLINE_PAGE", discipline);
    }

    generateDisciplines = () => {
        // Generate grid of existing disciplines basing on activeDiscipline stired in Redux
        const items = this.props.disciplines.filter(item => item.area === this.props.activeArea).sort().map(item => {
            const name = item.name.charAt(0).toUpperCase() + item.name.slice(1); // Capitalize first letter, ONLY FOR BUTTON LABEL
            return (
                <div>
                    <Card className="card" key={item.name} onClick={() => this.handleClick(item)}>
                        <Container className="card-body align-items-center d-flex justify-content-center">
                            <h4 className="card-title">{name}</h4>
                        </Container>
                    </Card>
                </div>
            )
        })

        return items;
    }
    render() {
        return (
            <Container>
                <div className="grid">
                    {this.generateDisciplines()}
                </div>
            </Container>
        );
    }
}

const mapStateToProps = (state) => {
    return {
        activeArea: state.activeArea,
        disciplines: state.disciplines,
    }
}

const mapDispatchToProps = (dispatch) => {
    return {
        updateActivePageAndDiscipline: (page, discipline) => { dispatch(updateActivePageAndDiscipline(page, discipline)) }
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(DisciplinesGrid);