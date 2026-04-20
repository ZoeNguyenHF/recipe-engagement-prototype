document.addEventListener('DOMContentLoaded', () => {
    const navItems = document.querySelectorAll('.nav-item:not(.has-dropdown)');
    const navSubItems = document.querySelectorAll('.nav-sub-item');
    const dropdownItems = document.querySelectorAll('.nav-item.has-dropdown');
    const pages = document.querySelectorAll('.page');
    const refreshIcons = document.querySelectorAll('.nav-refresh-icon');

    // Handle dropdown toggle
    dropdownItems.forEach(item => {
        item.addEventListener('click', (e) => {
            e.preventDefault();

            const dropdown = item.nextElementSibling;
            const isOpen = item.classList.contains('open');

            // Toggle dropdown
            if (isOpen) {
                item.classList.remove('open');
                dropdown.classList.remove('open');
            } else {
                item.classList.add('open');
                dropdown.classList.add('open');
            }

            // Also navigate to the parent page
            const pageId = item.getAttribute('data-page');
            if (pageId) {
                // Update active nav item
                navItems.forEach(nav => nav.classList.remove('active'));
                navSubItems.forEach(nav => nav.classList.remove('active'));
                item.classList.add('active');

                // Update active page
                pages.forEach(page => page.classList.remove('active'));
                const targetPage = document.getElementById(pageId);
                if (targetPage) {
                    targetPage.classList.add('active');
                }
            }
        });
    });

    // Handle regular nav items
    navItems.forEach(item => {
        item.addEventListener('click', (e) => {
            e.preventDefault();

            const pageId = item.getAttribute('data-page');

            // Update active nav item
            navItems.forEach(nav => nav.classList.remove('active'));
            navSubItems.forEach(nav => nav.classList.remove('active'));
            dropdownItems.forEach(nav => nav.classList.remove('active'));
            item.classList.add('active');

            // Update active page
            pages.forEach(page => page.classList.remove('active'));
            const targetPage = document.getElementById(pageId);
            if (targetPage) {
                targetPage.classList.add('active');
            }
        });
    });

    // Handle sub-items
    navSubItems.forEach(item => {
        item.addEventListener('click', (e) => {
            // Don't handle if clicking on refresh icon
            if (e.target.classList.contains('nav-refresh-icon')) {
                return;
            }

            e.preventDefault();

            const pageId = item.getAttribute('data-page');

            // Update active nav item
            navItems.forEach(nav => nav.classList.remove('active'));
            navSubItems.forEach(nav => nav.classList.remove('active'));
            dropdownItems.forEach(nav => nav.classList.remove('active'));
            item.classList.add('active');

            // Update active page
            pages.forEach(page => page.classList.remove('active'));
            const targetPage = document.getElementById(pageId);
            if (targetPage) {
                targetPage.classList.add('active');
            }
        });
    });

    // Handle refresh icons
    refreshIcons.forEach(icon => {
        icon.addEventListener('click', (e) => {
            e.preventDefault();
            e.stopPropagation();

            const pageId = icon.getAttribute('data-page');
            const targetPage = document.getElementById(pageId);

            if (targetPage) {
                // Find the iframe in this page and refresh it
                const iframe = targetPage.querySelector('iframe');
                if (iframe) {
                    // Reload the iframe by resetting its src
                    const src = iframe.src;
                    iframe.src = '';
                    setTimeout(() => {
                        iframe.src = src;
                    }, 10);
                }
            }
        });
    });
});
