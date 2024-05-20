import {Link} from 'react-router-dom'

export function Navigation() {

  return (
    <div>
        <Link to='/employeePage'><h1>Employee App</h1></Link>
        <Link to='/employee-create'>Create employee</Link>
    </div>
  )
}

export default Navigation