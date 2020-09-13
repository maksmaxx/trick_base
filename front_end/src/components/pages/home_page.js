import axios from "axios";
import React, { Component } from "react";
import { Spinner } from "react-bootstrap";
import { connect } from 'react-redux';
import { updateDisciplines } from "../../store/actions/actions";
import DisciplinesList from "../disciplines_list";


class HomePage extends Component {
    getDisciplines = () => {
        // Get disciplines from DB and dispatch store
        axios.get("https://trickbase.herokuapp.com/api/disciplines").then(
            // handle success
            result => {
                this.props.updateDisciplines(result.data.disciplines);
            }
        )
        .catch(function (error) {
            // handle error
            console.log(error);
          })
          .then(function () {
            // always executed
          });
    }
    componentDidMount() {
        this.getDisciplines();
    }
    render() {
        const view = this.props.disciplines ? (
            <DisciplinesList />
        ) : (
            <Spinner className="center" animation="border" role="status">
                <span className="sr-only">Loading...</span>
            </Spinner>
        );

        return view
    }
}

const mapStateToProps = (state) => {
    // Get state from Redux and pass to component's props
    return {
        disciplines: state.disciplines
    }
}

const mapDispatchToProps = (dispatch) => {
    // Pass dispatch method to props
    return {
        updateDisciplines: (disciplines) => { dispatch(updateDisciplines(disciplines)) }
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(HomePage);