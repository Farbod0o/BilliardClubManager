const socket = io();

socket.on('update', function(data) {
    const tableDiv = document.getElementById(`table-${data.table}`);
    if (data.status === 'started') {
        tableDiv.querySelector('button[onclick^="startGame"]').disabled = true;
        tableDiv.querySelector('button[onclick^="stopGame"]').disabled = false;
        tableDiv.querySelector('p span').innerText = 'در حال استفاده';
    } else if (data.status === 'stopped') {
        tableDiv.querySelector('button[onclick^="startGame"]').disabled = false;
        tableDiv.querySelector('button[onclick^="stopGame"]').disabled = true;
        tableDiv.querySelector('p span').innerText = 'خالی';
        const costSpan = tableDiv.querySelector('p span.cost');
        if (costSpan) {
            costSpan.innerText = `${data.cost} تومان`;
        }
    }
});

function startGame(tableId) {
    fetch(`/start/${tableId}`, { method: 'POST' });
}

function stopGame(tableId) {
    fetch(`/stop/${tableId}`, { method: 'POST' });
}

// ثبت Service Worker برای PWA
if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
        navigator.serviceWorker.register('/service-worker.js')
            .then((registration) => console.log('Service Worker registered:', registration))
            .catch((error) => console.log('Service Worker registration failed:', error));
    });
}
