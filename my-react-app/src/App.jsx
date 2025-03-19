import { useRef } from "react";

function App() {
  const inputRef = useRef(null); // Create a ref

  const focusInput = () => {
    inputRef.current.focus(); // Access the DOM element
  };

  return (
    <div>
      <input ref={inputRef} type="text" placeholder="Type here..." />
      <button onClick={focusInput}>Focus Input</button>
    </div>
  );
}

export default App;
