const initState = {
    activeArea: null,   // At Home page, active area is area chosen to display certain disciplines
    disciplines: null,  // All disciplines gotten from Axios(GET)
}

const rootReducer = (state = initState, action) => {
    if (action.type === "UPDATE_DISCIPLINES") {
        return {
            ...state,
            disciplines: action.disciplines
        }
    }
    
    if (action.type === "SET_ACTIVE_AREA") {
        return {
            ...state,
            activeArea: action.activeArea
        }
    }

    return state;
} 

export default rootReducer;