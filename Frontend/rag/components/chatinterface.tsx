'use client'
import React, { useState } from 'react'
import QueryInput from './Queryintput'
import ResponseDisplay from './ResponseDisplay'
import LoadingIndicator from './LoadingIndicator'
import { Card, CardHeader, CardContent  } from './ui/card'
import { Info } from 'lucide-react'

const ChatInterface = () => {
  const [messages, setMessages] = useState([])
  const [isLoading, setIsLoading] = useState(false)
  const handleSendQuery = async (query) => {
    setIsLoading(true)
    setMessages(prev => [...prev, { type: 'user', content: query }])
    try {
      const response = await fetch('/api', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: query, generate_audio: true }),
      })
      if (!response.ok) throw new Error('Network response was not ok')

      const data = await response.json()
      setMessages(prev => [...prev, { 
        type: 'assistant', 
        content: data.response,
        audio: data.audio,
        usedTool: data.used_tool,
      }])
    } catch (error) {
      console.error('Error:', error)
      setMessages(prev => [...prev, { 
        type: 'assistant', 
        content: 'Sorry, I encountered an error while processing your request.' 
      }])
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <Card className="w-full max-w-2xl mx-auto bg-white shadow-xl rounded-lg overflow-hidden">
    <div className="bg-gradient-to-r from-blue-500 to-purple-600 text-white px-6 py-3 flex  items-center">
      <Info className="mr-2" />
      <span className='text-xs font-extrabold'>This chat interface uses a large language model (LLM) and may provide inaccurate results. Use with caution.</span>
    </div>
    <CardContent className="h-[400px] overflow-y-auto p-6">
      <ResponseDisplay messages={messages} />
      {isLoading && <LoadingIndicator />}
    </CardContent>
    <div className="border-t p-4">
      <h2 className="text-3xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-blue-500 to-purple-600 text-center mb-4">
        Welcome to RAG-based Chat Assistant!
      </h2>
      <p className="text-md font-bold text-center text-gray-800 mb-6">
        Engage in a conversation and let your queries flow. I'm here to assist you!
      </p>
      <QueryInput onSendQuery={handleSendQuery} isLoading={isLoading} />
    </div>
  </Card>
  )
}

export default ChatInterface