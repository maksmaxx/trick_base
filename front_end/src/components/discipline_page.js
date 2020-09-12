import React, { Component } from 'react'
import { connect } from "react-redux";

class DisciplinePage extends Component {
    render() {
        return (
            <div className="container">
                { this.props.disciplineName }
            </div>
        )
    }
}

const mapStateToProps = (state, ownProps) => {
    let name = ownProps.match.params.discipline_name; // Derive discipline name from URI
    return {
        disciplineName: name
    }
}


export default connect(mapStateToProps)(DisciplinePage);