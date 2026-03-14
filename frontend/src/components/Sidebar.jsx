function Sidebar() {
  return (
    <div className="w-64 bg-[#202123] p-4 flex flex-col">

      <button className="border border-gray-500 rounded p-2 mb-4 hover:bg-gray-700">
        + New Chat
      </button>

      <div className="flex-1 overflow-y-auto">
        <p className="text-gray-400 text-sm">Chat History</p>
      </div>

    </div>
  )
}

export default Sidebar