fetch('/obec_bez_vs_s_mcmo_data')
    .then(response => response.json())
    .then(data => {
        // Vlastní názvy
        const customLabels = ["Obce mimo ÚnL", "Ústí nad Labem"];
        const values = data.data;

        // Vytvoření grafu pomocí Chart.js
        const ctx = document.getElementById('myChart4').getContext('2d');
        new Chart(ctx, {
            type: 'pie',
            data: {
                labels: customLabels,
                datasets: [{
                    label: 'Počty hlasů',
                    data: values,
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.5)',
                        'rgba(54, 162, 235, 0.5)'
                    ],
                    borderColor: [
                        'rgba(255, 99, 132, 1)',
                        'rgba(54, 162, 235, 1)'
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                plugins: {
                    legend: {
                        display: true,
                        position: 'top'
                    },
                    title: {
                        display: true,
                        text: 'Podíl hlasů obcí s a bez MCMO',
                        font: {
                            size: 18
                        }
                    }
                }
            }
        });
    })
    .catch(error => {
        console.error('Chyba při načítání dat:', error);
    });