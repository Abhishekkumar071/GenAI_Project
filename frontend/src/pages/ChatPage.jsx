import Sidebar from "../components/Sidebar"
import ChatBox from "../components/ChatBox"
import InputBox from "../components/InputBox"
import useChat from "../hooks/useChat"

function ChatPage() {

  const { messages, sendMessage, loading } = useChat()

  return (
    <div className="flex h-screen bg-[#343541] text-white">

      <Sidebar />

      <div className="flex flex-col flex-1">

        <ChatBox messages={messages} loading={loading} />

        <InputBox onSend={sendMessage} />

      </div>

    </div>
  )
}

export default ChatPage