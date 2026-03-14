import { useState } from "react"
import { sendMessageToBackend } from "../services/chatAPI"

export default function useChat() {

  const [messages, setMessages] = useState([])
  const [loading, setLoading] = useState(false)

  async function sendMessage(text) {

    if (!text.trim()) return

    const userMessage = {
      role: "user",
      content: text
    }

    setMessages(prev => [...prev, userMessage])

    setLoading(true)

    try {

      const aiReply = await sendMessageToBackend(text)

      const aiMessage = {
        role: "assistant",
        content: aiReply
      }

      setMessages(prev => [...prev, aiMessage])

    } catch (error) {

      const aiMessage = {
        role: "assistant",
        content: "Error connecting to backend"
      }

      setMessages(prev => [...prev, aiMessage])

    }

    setLoading(false)

  }

  return {
    messages,
    sendMessage,
    loading
  }

}