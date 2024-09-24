import React, { useState, useEffect } from 'react'

const loadingTexts = [
  "Applying processing...",
  "Extracting information...",
  "Generating response...",
  "Almost there...",
]
const LoadingIndicator = () => {
  const [textIndex, setTextIndex] = useState(0)
  useEffect(() => {
    const interval = setInterval(() => {
      setTextIndex((prevIndex) => (prevIndex + 1) % loadingTexts.length)
    }, 2000)
    return () => clearInterval(interval)
  }, [])

  return (
    <div className="flex items-center space-x-2 text-gray-500">
      <div className="animate-spin rounded-full h-4 w-4 border-t-2 border-b-2 border-gray-900"></div>
      <span>{loadingTexts[textIndex]}</span>
    </div>
  )
}

export default LoadingIndicator