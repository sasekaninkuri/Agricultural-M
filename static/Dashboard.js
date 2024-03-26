// Sample data for the charts
const barChartData = {
    labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
    datasets: [{
        label: 'Revenue',
        backgroundColor: 'rgba(54, 162, 235, 0.2)',
        borderColor: 'rgba(54, 162, 235, 1)',
        borderWidth: 1,
        data: [10000, 20000, 15000, 25000, 18000, 22000, 30000]
    }]
};

const lineChartData = {
    labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
    datasets: [{
        label: 'Sales',
        fill: false,
        borderColor: 'rgb(255, 99, 132)',
        data: [50, 60, 70, 65, 80, 75, 90]
    }]
};

// Create bar chart
var barChartCanvas = document.getElementById('barChart').getContext('2d');
var barChart = new Chart(barChartCanvas, {
    type: 'bar',
    data: barChartData,
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

    

    
