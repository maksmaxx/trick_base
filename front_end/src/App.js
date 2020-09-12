import React from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import DisciplinePage from './components/discipline_page';
import HomePage from './components/home_page';
import NavigationBar from './components/navigation_bar';

function App() {
  return (
    <BrowserRouter>
      <div className="App">
        <NavigationBar /> 
        <Switch>
          <Route exact path="/" component={HomePage} />
          <Route path="/disciplines/:discipline_name" component={DisciplinePage} />
        </Switch>
      </div>
    </BrowserRouter>
  );
}

export default App;
