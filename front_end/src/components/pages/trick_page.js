import React, { Component } from 'react'
import axios from 'axios';
import { connect } from "react-redux";
import { updateActiveTrick } from '../../store/actions/actions';
import { Container, ListGroup, ListGroupItem, Spinner } from 'react-bootstrap';

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
        if (this.props.activeTrick !== null) {

            const videos = this.props.activeTrick.videos.map(video => { 
                return <ListGroupItem className="embed-responsive embed-responsive-16by9 trick-video" key={video}>
                    <iframe className="embed-responsive-item" title={video} src={video} frameBorder="0" allowFullScreen></iframe>
                </ListGroupItem> 
            });
            
            const discipline = this.props.activeTrick.discipline.charAt(0).toUpperCase() + this.props.activeTrick.discipline.slice(1); // Capitalize first letter, ONLY FOR BUTTON LABEL
            const trick = this.props.activeTrick.name.charAt(0).toUpperCase() + this.props.activeTrick.name.slice(1);
            const category = this.props.activeTrick.category.charAt(0).toUpperCase() + this.props.activeTrick.category.slice(1);

            const view = this.props.activeTrick ? (
                <Container align="center">
                <h1 className="title"> {discipline + ": " + trick}</h1>
                <p className="description"> {category}</p>
                <ListGroup>
                    { videos }
                </ListGroup>
            </Container>
            ) : null;
        
            return view;
        }
        else {
            return <Spinner className="center" animation="border" role="status">
                <span className="sr-only">Loading...</span>
            </Spinner>
        }
        
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