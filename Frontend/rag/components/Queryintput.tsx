import React, { useState } from 'react'
import { Input } from './ui/input'
import { Button } from './ui/button'
import { Send } from 'lucide-react'

const QueryInput = ({ onSendQuery, isLoading }) => {
  const [query, setQuery] = useState('')
  const handleSubmit = (e) => {
    e.preventDefault()
    if (query.trim() && !isLoading) {
      onSendQuery(query)
      setQuery('')
    }
  }

  return (
    <form onSubmit={handleSubmit} className="flex space-x-2">
      <Input
        type="text"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Type your message here..."
        disabled={isLoading}
        className="flex-grow"
      />
      <Button type="submit" disabled={isLoading}>
        <Send className="h-4 w-4" />
      </Button>
    </form>
  )
}

export default QueryInput