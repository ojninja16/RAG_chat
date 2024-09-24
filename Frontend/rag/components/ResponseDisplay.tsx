import React from 'react'
import AudioPlayer from './AudioPlayer'
import { Badge } from '@/components/ui/badge'

const ResponseDisplay = ({ messages }) => {
    const getToolBadgeColor = (tool) => {
        switch (tool) {
          case 'rag':
            return 'bg-blue-500 text-white'
          case 'calculator':
            return 'bg-green-500 text-white'
          case 'greeting':
            return 'bg-yellow-500 text-white'
          case 'general_knowledge':
            return 'bg-purple-500 text-white'
          default:
            return 'bg-gray-400 text-gray-800'
        }
      }
  return (
    <div className="space-y-4">
      {messages.map((message, index) => (
        <div key={index} className={`flex ${message.type === 'user' ? 'justify-end' : 'justify-start'}`}>
          <div className={`max-w-[70%] p-3 rounded-lg ${
            message.type === 'user' ? 'bg-blue-500 text-white' : 'bg-gray-200 text-gray-800'
          }`}>
            {message.usedTool && (
              <div className="mb-2">
                <Badge className={getToolBadgeColor(message.usedTool)}>
                  {message.usedTool}
                </Badge>
              </div>
            )}
            <p>{message.content}</p>
            {message.audio && <AudioPlayer audioSrc={message.audio} />}
          </div>
        </div>
      ))}
    </div>
  )
}

export default ResponseDisplay