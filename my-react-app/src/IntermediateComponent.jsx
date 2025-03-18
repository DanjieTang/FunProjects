import React, { createContext } from 'react';
import MiddleComponent from './MiddleComponent';

// Create the context in this intermediate component
export const MyContext = createContext(null);

function IntermediateComponent() {
  return (
    <MyContext.Provider value={42}>
      <MiddleComponent />
    </MyContext.Provider>
  );
}

export default IntermediateComponent; 