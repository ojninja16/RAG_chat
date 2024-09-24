import React, { useRef, useEffect } from 'react'
import { Button } from './ui/button'
import { Play, Pause } from 'lucide-react'

const AudioPlayer = ({ audioSrc }) => {
  const audioRef = useRef(null)
  const [isPlaying, setIsPlaying] = React.useState(false)
  useEffect(() => {
    const audioElement = audioRef.current
    if (audioElement) {
       audioElement.addEventListener('ended', () => setIsPlaying(false))
       return () => {
        audioElement.removeEventListener('ended', () => setIsPlaying(false))
      }
    }
  }, [])
  const togglePlay = () => {
    if (audioRef.current.paused) {
      audioRef.current.play()
      setIsPlaying(true)
    } else {
      audioRef.current.pause()
      setIsPlaying(false)
    }
  }
  return (
    <div className="mt-2">
      <audio ref={audioRef} src={`data:audio/wav;base64,${audioSrc}`} />
      <Button onClick={togglePlay} variant="outline" size="sm">
        {isPlaying ? <Pause className="h-4 w-4" /> : <Play className="h-4 w-4" />}
      </Button>
    </div>
  )
}

export default AudioPlayer