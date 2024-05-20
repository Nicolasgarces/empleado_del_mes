import axios from 'axios'

export const getAllEmployees = () => {
   return axios.get('http://localhost:8000/api/persons/')
}

export default getAllEmployees