import React, { Component } from 'react'
import { connect } from "react-redux";
import axios from 'axios';
import { updateActiveTricks } from '../../store/actions/actions';
import TricksGrid from '../tricks_grid';

class DisciplinePage extends Component {
    getTricks = () => {
        // Always clear tricks in the cache
        this.props.updateActiveTricks(null); 

        // Get disciplines from DB and dispatch store
        // POST    /api/tricks : Get all tricks belonging to discipline identified by "name"
        axios.post('https://trickbase.herokuapp.com/api/tricks', {
            discipline: this.props.disciplineName,
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
        
        return (
            <div className="container">
                { this.props.disciplineName }
                <TricksGrid />
            </div>
        )
    }
}

const mapStateToProps = (state, ownProps) => {
    let name = ownProps.match.params.discipline_name; // Derives discipline name from URI
    return {
        disciplineName: name,
        activeTricks: state.activeTricks
    }
}

const mapDispatchToProps = (dispatch) => {
    // Pass dispatch method to props
    return {
        updateActiveTricks: (tricks) => { dispatch(updateActiveTricks(tricks)) }
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(DisciplinePage);