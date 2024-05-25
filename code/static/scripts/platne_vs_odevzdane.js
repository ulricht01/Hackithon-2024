fetch('/platne_vs_odevzdane_hlasy_data')
    .then(response => response.json())
    .then(data => {
        const values = data.data;

        // Vlastní názvy
        const customNames = ["Obce mimo ÚnL", "Ústí nad Labem"];

        document.getElementById('titleName').textContent = ['Neplatné hlasy']
        // Nastavení názvů a hodnot do obdélníků
        document.getElementById('name1').textContent = customNames[0];
        document.getElementById('value1').textContent = values[0];
        document.getElementById('name2').textContent = customNames[1];
        document.getElementById('value2').textContent = values[1];

    })
    .catch(error => {
        console.error('Chyba při načítání dat:', error);
    });