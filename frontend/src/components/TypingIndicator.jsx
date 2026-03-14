function TypingIndicator() {

  return (
    <div className="flex mb-4">

      <div className="bg-gray-700 px-4 py-2 rounded-lg flex gap-1">

        <span className="animate-bounce">.</span>
        <span className="animate-bounce delay-150">.</span>
        <span className="animate-bounce delay-300">.</span>

      </div>

    </div>
  )
}

export default TypingIndicator