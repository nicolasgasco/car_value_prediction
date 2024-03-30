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
  const [userMileage, setUserMileage] = useState<number>(40_000)
  const { current: predictionsData } = useRef<PredictionsData>(predictions)
  const [gradientPercentage, setGradientPercentage] = useState<number>(0)

  const handleUserMileageChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const mileage = Number(event.target.value)
    setUserMileage(mileage)

    setGradientPercentage(mileage * 400 / Number(predictionsData.max_value))
  }

  const formatPricePrediction = (price: string) => {
    const priceAsNumber = Number(price);
    return priceAsNumber.toLocaleString();
  }

  const formatMileage = (mileage: number) => {
    return mileage.toLocaleString();
  }

  const gradientCss = (percentage: number) => {
    return `linear-gradient(
      ${percentage}deg,
      #fcb667 0%,
      #f8ab68 10%,
      #f2a06a 20%,
      #ec966b 30%,
      #e48d6d 40%,
      #e08871 50%,
      #da8375 60%,
      #d47f79 70%,
      #d07e7f 80%,
      #cb7e85 90%,
      #c67e8b 100%,
      #c07e8f
    )`;
  }

  return (
    <>
      <h1 className="mb-16">Car price estimate</h1>
      <p className="mb-32">How much is my 2019-2020 Opel Corsa worth?</p>

      <main>
        <h2 className="mb-8">Mileage</h2>
        <div className="container">
          <div className="mileage-selector">
            <p className="mb-16">Choose the mileage of your vehicle.</p>

            <div className="mb-8">
              <label className='sr-only' htmlFor="mileage-input">Mileage</label>
              <input type="number" min={predictionsData.min_value} max={predictionsData.max_value} step="1000" placeholder="Add your vehicle mileage" value={userMileage} id="mileage-input" onChange={handleUserMileageChange} />
            </div>

            <div>
              <label className='sr-only' htmlFor="mileage-slider">Mileage</label>
              <input type="range" min={predictionsData.min_value} max={predictionsData.max_value} step="10000" value={userMileage} id="mileage-slider" className="slider" onChange={handleUserMileageChange} />
            </div>
          </div>

          <div className="result-container" style={{ backgroundImage: gradientCss(gradientPercentage) }}>
            <p>Your vehicle with {formatMileage(userMileage)} km<br />is worth <span className="highlight">€{formatPricePrediction(predictionsData.predictions[userMileage])}</span>.</p>
          </div>
        </div>
      </main>

    </>
  )
}

export default App
