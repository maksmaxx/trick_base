const initState = {
    activePage: "HOME_PAGE",    // Current displayed page
    activeArea: null,           // At Home page, active area is area chosen to display certain disciplines
    activeDiscipline: null,     // etc.
    activeTrick: null,          // All tricks displayed after when discipline's chosen
    activeTricks: null,         // At Disicpline Page: tricks to be shown belonging to certain discipline
    disciplines: null,          // All cached disciplines gotten from Axios(GET)
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

    if (action.type === "UPDATE_ACTIVE_PAGE") {
        return {
            ...state,
            activePage: action.activePage
        }
    }

    if (action.type === "UPDATE_ACTIVE_PAGE_AND_DISCIPLINE") {
        return {
            ...state,
            activePage: action.activePage,
            activeDiscipline: action.activeDiscipline
        }
    }

    if (action.type === "UPDATE_ACTIVE_PAGE_AND_TRICK") {
        return {
            ...state,
            activePage: action.activePage,
            activeTrick: action.activeTrick
        }
    }

    return state;
} 

export default rootReducer;