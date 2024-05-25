fetch('/min_prc_ucast_data').then(response => response.json()).then(data => {
    const labels = data.labels;
    const zaznamy = data.data;

    // Vytvoření grafu pomocí Chart.js
    const ctx = document.getElementById('myChart2').getContext('2d');
    new Chart(ctx, {
        type: 'bar', // změna typu grafu na sloupcový
        data: {
            labels: labels,
            datasets: [{
                label: '%',
                data: zaznamy,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.5)',
                    'rgba(54, 162, 235, 0.5)',
                    'rgba(255, 206, 86, 0.5)',
                    'rgba(75, 192, 192, 0.5)',
                    'rgba(153, 102, 255, 0.5)',
                    'rgba(255, 159, 64, 0.5)'
                ]
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
                    position: 'left'
                },
                title: {
                    display: true,
                    text: '5 Nejnižších volebních účastí',
                    font: {
                        size: 18
                    }
                }
            }
        }
    });
}).catch(error => {
    console.error('Chyba při načítání dat:', error);
});