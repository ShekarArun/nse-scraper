< !DOCTYPE html >
    <html lang="en">
        <head>
            <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Fetch and Save CSV</title>
                </head>
                <body>
                    <button id="fetchData">Fetch and Save Data</button>

                    <script>
        document.getElementById('fetchData').addEventListener('click', async () => {
            const url = 'https://www.nseindia.com/api/live-analysis-oi-spurts-underlyings';

                        try {
                const response = await fetch(url, {
                            headers: {
                            'User-Agent': 'Mozilla/5.0', // This header might not be allowed in fetch
                        'Accept': 'application/json',
                    }
                });

                        if (!response.ok) {
                    throw new Error('Network response was not ok');
                }

                        const jsonData = await response.json();
                        const data = jsonData.data;

                        // Convert JSON to CSV
                        const csvRows = [];
                        const headers = Object.keys(data[0]);
                        csvRows.push(headers.join(','));

                        for (const row of data) {
                    const values = headers.map(header => JSON.stringify(row[header], replacer));
                        csvRows.push(values.join(','));
                }

                        const csvData = csvRows.join('\n');
                        const blob = new Blob([csvData], {type: 'text/csv' });
                        const url = URL.createObjectURL(blob);

                        const a = document.createElement('a');
                        a.setAttribute('hidden', '');
                        a.setAttribute('href', url);
                        a.setAttribute('download', 'underlyings.csv');
                        document.body.appendChild(a);
                        a.click();
                        document.body.removeChild(a);

            } catch (error) {
                            console.error('Error fetching data:', error);
            }
        });

                        function replacer(key, value) {
            return value === null ? '' : value;
        }
                    </script>
                </body>
            </html>