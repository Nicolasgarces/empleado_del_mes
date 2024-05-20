import {BrowserRouter, Routes, Route, Navigate} from 'react-router-dom'
import EmployeePage from './pages/EmployeePage'
import EmployeeFormPage from './pages/EmployeeFormPage'
import Navigation from './components/Navigation'

function App() {
  return (
    <BrowserRouter>
    <Navigation/>
      <Routes>
        <Route path='/' element={<Navigate to='/employeePage'/>}/>

        <Route path='/employeePage' element={<EmployeePage/>}/>

        <Route path='/employee-create' element={<EmployeeFormPage/>} />

      </Routes>

    
    </BrowserRouter>
  )
}

export default App