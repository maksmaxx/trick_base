import React, { Component } from 'react'
import axios from 'axios';
import { connect } from "react-redux";
import { updateActiveTrick } from '../../store/actions/actions';

class TrickPage extends Component {
    getTrick = () => {
        // Always clear tricks in the cache
        this.props.updateActiveTrick(null); 

        // Get trick from DB and dispatch store
        axios.get('https://trickbase.herokuapp.com/api/tricks/' + this.props.trickId)
         .then( response => {
             // handle Success
             this.props.updateActiveTrick(response.data);
         })
         .catch(error => {
             // handle error
           console.log(error);
        });
    }

    componentDidMount() {
        this.getTrick();
    }


    render() {
        const view = this.props.activeTrick ? (
            <div className="container">
                <p> {this.props.activeTrick.uuid}</p>
                <p> {this.props.activeTrick.name}</p>
                <p> {this.props.activeTrick.discipline}</p>
                <p> {this.props.activeTrick.category}</p>
                <p> {this.props.activeTrick.videos}</p>
            </div>
        ) : (
            <div className="container">
                <p> Loading </p>
            </div>
        );
        
        return view;
    }
}

const mapStateToProps = (state, ownProps) => {
    let id = ownProps.match.params.trick_id; // Derives discipline name from URI
    return {
        trickId: id,
        activeTrick: state.activeTrick
    }
}

const mapDispatchToProps = (dispatch) => {
    // Pass dispatch method to props
    return {
        updateActiveTrick: (trick) => { dispatch(updateActiveTrick(trick)) }
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(TrickPage);