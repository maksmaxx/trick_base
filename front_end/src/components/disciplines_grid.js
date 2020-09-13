import React, { Component } from "react";
import { Container } from "react-bootstrap";
import { connect } from "react-redux";
import { Link } from "react-router-dom";

class DisciplinesGrid extends Component  {
    generateDisciplines = () => {
        // Generate grid of existing disciplines basing on activeDiscipline stired in Redux
        const items = this.props.disciplines.filter(item => item.area === this.props.activeArea).map(item => {
            const name = item.name.charAt(0).toUpperCase() + item.name.slice(1); // Capitalize first letter, ONLY FOR BUTTON LABEL
            return (
                <Link to={'/disciplines/' + item.name} key={item.name}>
                    <div>{name}</div>
                </Link>
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
    // Get state from Redux and pass to component's props
    return {
        activeArea: state.activeArea,
        disciplines: state.disciplines,
    }
}

export default connect(mapStateToProps)(DisciplinesGrid);