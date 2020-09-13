import React, { Component } from 'react';
import { connect } from "react-redux";
import DisciplinePage from './components/pages/discipline_page';
import HomePage from './components/pages/home_page';
import NavigationBar from './components/navigation_bar';
import TrickPage from './components/pages/trick_page';
import Footer from './components/footer';

class App extends Component {
  assignPage = () => {
    const page = this.props.activePage;
    if (page === "HOME_PAGE") return <HomePage />
    if (page === "DISCIPLINE_PAGE") return <DisciplinePage />
    if (page === "TRICK_PAGE") return <TrickPage />
    else return <HomePage />
  }

  render() {
    const page = this.assignPage();
    return (
        <div className="App">
          <NavigationBar /> 
          { page }
          <Footer />
        </div>
    );
  }
}

const mapStateToProps = (state) => {
  return {
      activePage: state.activePage
  }
}

export default connect(mapStateToProps)(App);
