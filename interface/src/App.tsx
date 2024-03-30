import { useRef, useState } from 'react'
import predictions from '../data/predictions.json';

import './App.css'

function App() {
  const [userMileage, setUserMileage] = useState<number>(0)
  const { current: predictionsData } = useRef(predictions)

  const handleUserMileageChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setUserMileage(Number(event.target.value))
  }


  return (
    <>
      <h1>Car price estimate</h1>
      <p>How much is my 2019-2020 Open Corsa worth?</p>

      <div>
        <label htmlFor="mileage">Mileage</label>
        <input type="range" min={predictionsData.min_value} max={predictionsData.max_value} step="10000" value={userMileage} id="mileage" onChange={handleUserMileageChange} />
        <p>{userMileage.toLocaleString()}</p>
        <input type="text" value={userMileage} onChange={handleUserMileageChange} />
      </div>
    </>
  )
}

export default App
