fetch('/volby_1_data')
    .then(response => response.json())
    .then(data => {
        const labels = data.labels;
        const values = data.data;

        // Vytvoření grafu pomocí Chart.js
        const ctx = document.getElementById('myChart').getContext('2d');
        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Celkem hlasů',
                    data: values,
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.5)',
                        'rgba(54, 162, 235, 0.5)',
                        'rgba(255, 206, 86, 0.5)',
                        'rgba(75, 192, 192, 0.5)',
                        'rgba(153, 102, 255, 0.5)'
                    ],
                    borderColor: [
                        'rgba(255, 99, 132, 1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 206, 86, 1)',
                        'rgba(75, 192, 192, 1)',
                        'rgba(153, 102, 255, 1)'
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                },
                plugins: {
                    legend: {
                        display: false,
                        position: 'top'
                    },
                    title: {
                        display: true,
                        text: 'Top 5 Stran dle Počtu Hlasů',
                        font: {
                            size: 18
                        }
                    },
                    datalabels: {
                        anchor: 'end',
                        align: 'top',
                        formatter: (value) => value, // formátování popisků
                        font: {
                            weight: 'bold'
                        }
                    }
                }
            },
            // Include the ChartDataLabels plugin
            plugins: [ChartDataLabels]
        });
    })
    .catch(error => {
        console.error('Chyba při načítání dat:', error);
    });
