async function getData() {
    const response = await fetch('http://localhost:3000/api/names', { cache: 'no-store' }); // URL needs to be absolute for server-side fetch
    if (!response.ok) {
        throw new Error('Failed to fetch data');
    }
    return response.json();
}

export default async function Page() {
    const data = await getData();

    return (
        <div>
            <h1>Hello world</h1>
            <pre>{JSON.stringify(data, null, 2)}</pre>
        </div>
    );
}