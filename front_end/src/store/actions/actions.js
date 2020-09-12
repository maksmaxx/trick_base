export const updateDisciplines = (disciplines) => {
    return {
        type: "UPDATE_DISCIPLINES",
        disciplines: disciplines
    }
}

export const setActiveArea = (area) => {
    return {
        type: "SET_ACTIVE_AREA",
        activeArea: area
    }
}