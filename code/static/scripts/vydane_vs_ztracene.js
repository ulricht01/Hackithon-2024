fetch('/vydane_vs_ztracene_hlasy_data')
    .then(response => response.json())
    .then(data => {
        const values = data.data;

        // Vlastní názvy
        const customNames = ["Obce mimo ÚnL", "Ústí nad Labem"];

        document.getElementById('titleName2').textContent = ['Ztracené hlasy']
        // Nastavení názvů a hodnot do obdélníků
        document.getElementById('name3').textContent = customNames[0];
        document.getElementById('value3').textContent = values[0];
        document.getElementById('name4').textContent = customNames[1];
        document.getElementById('value4').textContent = values[1];

    })
    .catch(error => {
        console.error('Chyba při načítání dat:', error);
    });

fetch('/vydane_vs_ztracene_hlasy_data')
    .then(response => response.json())
    .then(data => {
        const values = data.data;
        const customNames = ["Obce mimo ÚnL", "Ústí nad Labem"];
        const colors = ['#FF6384', '#36A2EB']; // Barvy pro segmenty koláče

        // Nastavení dat pro graf
        const ctx = document.getElementById('myChart2').getContext('2d');
        new Chart(ctx, {
            type: 'pie',
            data: {
                labels: customNames,
                datasets: [{
                    data: values,
                    backgroundColor: colors
                }]
            },
            options: {
                plugins: {
                    title: {
                        display: true,
                        text: 'Ztracené hlasy',
                        font: {
                            size: 18
                        }
                    },
                    legend: {
                        position: 'top'
                    },
                    datalabels:{
                        datalabels:{
                            anchor: 'end',
                        align: 'top',
                        formatter: (values) => values, // formátování popisků
                        font: {
                            weight: 'bold'
                        }
                        }
                    }
                }
            },
            plugins: [ChartDataLabels] // přidání pluginu do grafu
        });
    })
    .catch(error => {
        console.error('Chyba při načítání dat:', error);
    });