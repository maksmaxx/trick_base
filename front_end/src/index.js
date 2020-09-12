import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import './index.css';
import * as serviceWorker from './serviceWorker';
import { createStore } from 'redux';
import rootReducer from './store/reducers/root_reducer';
import { Provider } from 'react-redux';
import 'bootstrap/dist/css/bootstrap.min.css'; // Required for Bootstrap to work

const store = createStore(rootReducer) // A redux Store for the whole app

ReactDOM.render(
  <React.StrictMode>
    <Provider store={store}>
      <App />
    </Provider>
  </React.StrictMode>,
  document.getElementById('root')
);

serviceWorker.unregister();
