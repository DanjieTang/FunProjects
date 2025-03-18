import React from 'react';
import Children from './Children';

function MiddleComponent() {
  return (
    <div>
      <h2>Middle Component</h2>
      <Children />
    </div>
  );
}

export default MiddleComponent; 