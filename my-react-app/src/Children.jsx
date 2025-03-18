import React, { useContext } from 'react';
import { MyContext } from './IntermediateComponent';

function Children() {
    const value = useContext(MyContext);
    return (
        <div>
            <h1>Children</h1>
            <h1>{value}</h1>
        </div>
    );
}

export default Children;