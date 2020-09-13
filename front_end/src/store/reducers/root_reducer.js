const initState = {
    activeArea: null,   // At Home page, active area is area chosen to display certain disciplines
    activeTrick: null,
    activeTricks: null,       // At Disicpline Page: tricks to be shown belonging to certain discipline
    disciplines: null,  // All disciplines gotten from Axios(GET)
}

const rootReducer = (state = initState, action) => {
    if (action.type === "UPDATE_DISCIPLINES") {
        return {
            ...state,
            disciplines: action.disciplines
        }
    }
    
    if (action.type === "UPDATE_ACTIVE_AREA") {
        return {
            ...state,
            activeArea: action.activeArea
        }
    }

    if (action.type === "UPDATE_ACTIVE_TRICKS") {
        return {
            ...state,
            activeTricks: action.activeTricks
        }
    }

    if (action.type === "UPDATE_ACTIVE_TRICK") {
        return {
            ...state,
            activeTrick: action.activeTrick
        }
    }

    return state;
} 

export default rootReducer;