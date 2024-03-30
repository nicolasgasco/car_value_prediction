import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [userMileage, setUserMileage] = useState<number>(0)

  const handleUserMileageChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setUserMileage(Number(event.target.value))
  }

  return (
    <>
      <h1>Car price estimate</h1>
      <p>How much is my 2019-2020 Open Corsa worth?</p>

      <div>
        <label htmlFor="mileage">Mileage</label>
        <input type="range" min="1000" max="200000" step="1000" value={userMileage} id="mileage" onChange={handleUserMileageChange} />
        <p>{userMileage}</p>
      </div>
    </>
  )
}

export default App
