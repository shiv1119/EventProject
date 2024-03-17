import { createStore, applyMiddleware, compose } from 'redux'
import { thunk } from 'redux-thunk'
import rootReducer from './reducers'

const initialState = {}
const middlewareEnhancer = applyMiddleware(thunk)
const composeWithDevTools =
  window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose
const composedEnhancers = composeWithDevTools(middlewareEnhancer)

const store = createStore(rootReducer, initialState, composedEnhancers)

export default store
