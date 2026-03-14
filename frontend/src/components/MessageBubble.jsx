function MessageBubble({ message }) {

  const isUser = message.role === "user"

  return (
    <div className={`flex mb-4 ${isUser ? "justify-end" : "justify-start"}`}>

      <div
        className={`px-4 py-2 rounded-lg max-w-xl
        ${isUser ? "bg-blue-600" : "bg-gray-700"}`}
      >
        {message.content}
      </div>

    </div>
  )
}

export default MessageBubble