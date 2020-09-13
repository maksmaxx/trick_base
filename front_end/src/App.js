import React from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import DisciplinePage from './components/pages/discipline_page';
import HomePage from './components/pages/home_page';
import NavigationBar from './components/navigation_bar';
import TrickPage from './components/pages/trick_page';

function App() {
  return (
    <BrowserRouter>
      <div className="App">
        <NavigationBar /> 
        <Switch>
          <Route exact path="/" component={HomePage} />
          <Route path="/disciplines/:discipline_name" component={DisciplinePage} />
          <Route path="/tricks/:trick_id" component={TrickPage} />
        </Switch>
      </div>
    </BrowserRouter>
  );
}

export default App;
