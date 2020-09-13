export const updateDisciplines = (disciplines) => {
    return {
        type: "UPDATE_DISCIPLINES",
        disciplines: disciplines
    }
}

export const updateActiveArea = (area) => {
    return {
        type: "UPDATE_ACTIVE_AREA",
        activeArea: area
    }
}

export const updateActiveTricks = (tricks) => {
    return {
        type: "UPDATE_ACTIVE_TRICKS",
        activeTricks: tricks
    }
}

export const updateActiveTrick = (trick) => {
    return {
        type: "UPDATE_ACTIVE_TRICK",
        activeTrick: trick
    }
}

export const updateActivePage = (page) => {
    return {
        type: "UPDATE_ACTIVE_PAGE",
        activePage: page
    }
}

export const updateActivePageAndDiscipline = (page, discipline) => {
    return {
        type: "UPDATE_ACTIVE_PAGE_AND_DISCIPLINE",
        activePage: page,
        activeDiscipline: discipline
    }
}

export const updateActivePageAndTrick = (page, trick) => {
    return {
        type: "UPDATE_ACTIVE_PAGE_AND_TRICK",
        activePage: page,
        activeTrick: trick
    }
}
