import { useState } from "react"

function InputBox({ onSend }) {

  const [input, setInput] = useState("")

  function handleSend() {

    if (!input.trim()) return

    onSend(input)

    setInput("")
  }

  return (
    <div className="p-4 border-t border-gray-700">

      <div className="flex gap-2">

        <input
          className="flex-1 p-3 rounded bg-gray-800 outline-none"
          placeholder="Send a message..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
        />

        <button
          onClick={handleSend}
          className="bg-green-600 px-4 rounded"
        >
          Send
        </button>

      </div>

    </div>
  )
}

export default InputBox