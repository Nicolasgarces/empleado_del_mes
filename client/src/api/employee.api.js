import axios from 'axios'

const peopleApi = axios.create({
   baseURL: 'http://localhost:8000/api/persons/'
})

export const getAllPeople = () => peopleApi.get('/');

export const createPerson = (person) => peopleApi.post("/", person)