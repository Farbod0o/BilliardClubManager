// service-worker.js
self.addEventListener('install', (event) => {
    console.log('Service Worker: Installed');
    // در صورت نیاز می‌توانید فایل‌ها را برای کارکرد آفلاین کش کنید
});

self.addEventListener('fetch', (event) => {
    event.respondWith(fetch(event.request).catch(() => {
        // نمایش یک پاسخ جایگزین در صورت آفلاین بودن
        return new Response('شما به اینترنت دسترسی ندارید.');
    }));
});
