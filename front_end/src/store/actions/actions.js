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
