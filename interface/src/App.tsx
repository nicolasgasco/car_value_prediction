import { useRef, useState } from 'react'
import predictions from '../data/predictions.json';

import './App.css'

interface PredictionsData {
  min_value: string;
  max_value: string;
  predicted_at: string;
  scraped_at: string;
  predictions: object;
}

function App() {
  const [userMileage, setUserMileage] = useState<number>(0)
  const { current: predictionsData } = useRef<PredictionsData>(predictions)

  const handleUserMileageChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setUserMileage(Number(event.target.value))
  }

  const formatPricePrediction = (price: string) => {
    const priceAsNumber = Number(price);
    return priceAsNumber.toLocaleString();
  }

  return (
    <>
      <h1>Car price estimate</h1>
      <p>How much is my 2019-2020 Opel Corsa worth?</p>

      <div>
        <div>
          <label htmlFor="mileage-slider">Mileage</label>
          <input type="range" min={predictionsData.min_value} max={predictionsData.max_value} step="10000" value={userMileage} id="mileage-slider" onChange={handleUserMileageChange} />
          <p>{userMileage.toLocaleString()}</p>
        </div>

        <div>
          <label htmlFor="mileage-input">Mileage</label>
          <input type="text" value={userMileage} id="mileage-input" onChange={handleUserMileageChange} />
        </div>
      </div>

      <p>Your Opel corsa is worth €{formatPricePrediction(predictionsData.predictions[userMileage])} </p>
    </>
  )
}

export default App
