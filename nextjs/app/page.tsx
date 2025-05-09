"use client";

import { useEffect, useState } from 'react';

interface ApiResponse {
    message?: string;
    received?: any;
}

export default function Page() {
    const [data, setData] = useState<ApiResponse | null>(null);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await fetch('/api/names');
                const result: ApiResponse = await response.json();
                setData(result);
            } catch (error) {
                console.error("Failed to fetch data:", error);
            }
        };

        fetchData();
    }, []);

    return (
        <div>
            <h1>Hello world</h1>
            {data && <pre>{JSON.stringify(data, null, 2)}</pre>}
        </div>
    );
}