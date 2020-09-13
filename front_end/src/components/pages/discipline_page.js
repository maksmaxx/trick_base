import React, { Component } from 'react'
import axios from 'axios';
import { connect } from "react-redux";
import { Container } from 'react-bootstrap';
import { updateActiveTricks } from '../../store/actions/actions';
import TricksGrid from '../tricks_grid';

class DisciplinePage extends Component {
    // Shows discipline page - name and tricks belonging to discipline
    
    getTricks = () => {
        this.props.updateActiveTricks(null); // Always clear tricks in the cache

        // POST    /api/tricks : Get all tricks belonging to discipline identified by "name"
        axios.post('https://trickbase.herokuapp.com/api/tricks', {
            discipline: this.props.activeDiscipline.name,
         })
         .then( response => {
             // handle Success
             this.props.updateActiveTricks(response.data.tricks);
         })
         .catch(error => {
             // handle error
           console.log(error);
        });
    }

    componentDidMount() {
        this.getTricks();
    }

    render() {
        // Capitalize first letter of discipline's name
        const name = this.props.activeDiscipline.name.charAt(0).toUpperCase() + this.props.activeDiscipline.name.slice(1);
        
        return (
            <Container align="center">
                <h1 className="title"> {name} </h1>
                <TricksGrid />
            </Container>
        )
    }
}

const mapStateToProps = (state) => {
    return {
        activeDiscipline: state.activeDiscipline,
        activeTricks: state.activeTricks
    }
}

const mapDispatchToProps = (dispatch) => {
    return {
        updateActiveTricks: (tricks) => { dispatch(updateActiveTricks(tricks)) }
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(DisciplinePage);