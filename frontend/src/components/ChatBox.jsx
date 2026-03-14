import MessageBubble from "./MessageBubble"
import TypingIndicator from "./TypingIndicator"

function ChatBox({ messages, loading }) {

  return (
    <div className="flex-1 overflow-y-auto p-6">

      {messages.map((msg, index) => (
        <MessageBubble key={index} message={msg} />
      ))}

      {loading && <TypingIndicator />}

    </div>
  )
}

export default ChatBox