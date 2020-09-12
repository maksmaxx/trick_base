import React, { Component } from "react";
import { ButtonGroup, Container, Button} from "react-bootstrap";
import { connect } from "react-redux";
import DisciplinesGrid from "./disciplines_grid";
import { setActiveArea } from "../store/actions/actions";

class DisciplinesList extends Component {
    handleAreaButton = (area) => {
        this.props.setActiveArea(area);
    }

    generateAreaButtons = () => {
        // Get areas from disciplines stored in redux store
        const areas = this.props.disciplines.map(item => {
            var area = item.area
            return area
        }).filter((v, i, a) => a.indexOf(v) === i); // Eliminates duplicate values

        if (this.props.activeArea === null) { // Set default area = first item from areas
            this.props.setActiveArea(areas[0]);
        }

        // Create unique buttons 
        const buttons = areas.map(item => {
            const name = item.charAt(0).toUpperCase() + item.slice(1); // Capitalize first letter, ONLY FOR BUTTON LABEL
            return <Button variant="secondary" key={item} onClick={() => this.handleAreaButton(item) }>{name}</Button>
        })
        
        // Return Component - button group
        return (
            <ButtonGroup className="overflow-auto">
                { buttons }
            </ButtonGroup>
        );
    }

    render() {
        return (
            <div className="disciplines-list">
                <Container className="d-flex justify-content-center">
                    { this.generateAreaButtons() }   
                </Container>
                <DisciplinesGrid />
            </div>
        );
    }
}

const mapDispatchToProps = (dispatch) => {
    // Pass dispatch method to props
    return {
        setActiveArea: (area) => { dispatch(setActiveArea(area)) }
    }
}

const mapStateToProps = (state) => {
    // Get state from Redux and pass to component's props
    return {
        activeArea: state.activeArea,
        disciplines: state.disciplines,
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(DisciplinesList);