import React, { Component } from 'react'
import { connect } from "react-redux";
import { Container, ListGroup, ListGroupItem } from 'react-bootstrap';

class TrickPage extends Component {
    // Shows trick page with associated videos

    render() {
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
    }


const mapStateToProps = (state) => {
    return {
        activeTrick: state.activeTrick
    }
}

export default connect(mapStateToProps)(TrickPage);