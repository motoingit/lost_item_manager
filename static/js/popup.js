(function () {
    // Encapsulate popup behavior and expose a small API.
    const popup = document.getElementById('action-popup');
    if (!popup) return;

    function showPopup() {
        popup.classList.remove('hide');
        popup.classList.add('show');

        // Auto-hide after 5 seconds
        clearTimeout(popup._hideTimer);
        popup._hideTimer = setTimeout(() => {
            hidePopup();
        }, 5000);
    }

    function hidePopup() {
        popup.classList.remove('show');
        popup.classList.add('hide');
        clearTimeout(popup._hideTimer);
    }

    // Attach to any buttons with .btn-popup so other parts of the UI can opt-in
    const triggerButtons = document.querySelectorAll('.btn-popup');
    triggerButtons.forEach(btn => btn.addEventListener('click', showPopup));

    // Expose a global function so templates or other scripts can trigger the popup
    window.showActionPopup = showPopup;
    window.hideActionPopup = hidePopup;

    // If the page is loaded with ?action=undo or ?action=redo (set by server redirects),
    // automatically show the popup once. This makes undo/redo routes able to signal the UI.
    try {
        const params = new URLSearchParams(window.location.search);
        if (params.has('action')) {
            // show immediately (don't rely on load event which may have already fired)
            // small defer so CSS classes can be applied
            requestAnimationFrame(() => showPopup());
            // remove the action param from the URL so refresh won't retrigger
            if (history && history.replaceState) {
                const url = new URL(window.location.href);
                url.searchParams.delete('action');
                history.replaceState({}, document.title, url.pathname + url.search);
            }
        }
    } catch (e) {
        // ignore URL parsing errors
        console.error('popup.js: failed to parse URL params', e);
    }
})();
