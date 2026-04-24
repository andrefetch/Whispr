(function () {
    var TOAST_DURATION = 5000;
    var toasts = document.querySelectorAll('[data-toast]');
    if (!toasts.length) return;

    var dismiss = function (toast) {
        if (toast.classList.contains('is-hiding')) return;
        toast.classList.add('is-hiding');
        var remove = function () { if (toast.parentNode) toast.parentNode.removeChild(toast); };
        toast.addEventListener('transitionend', remove, { once: true });
        setTimeout(remove, 500);
    };

    toasts.forEach(function (toast, i) {
        toast.style.setProperty('--toast-delay', (i * 100) + 'ms');
        toast.style.setProperty('--toast-duration', TOAST_DURATION + 'ms');

        var closeBtn = toast.querySelector('[data-toast-close]');
        if (closeBtn) closeBtn.addEventListener('click', function () { dismiss(toast); });

        var progress = toast.querySelector('.toast-progress');
        var fallback = setTimeout(function () { dismiss(toast); }, TOAST_DURATION + i * 100 + 600);
        if (progress) {
            progress.addEventListener('animationend', function () {
                clearTimeout(fallback);
                dismiss(toast);
            });
        }

        toast.addEventListener('mouseenter', function () { toast.classList.add('is-paused'); });
        toast.addEventListener('mouseleave', function () { toast.classList.remove('is-paused'); });
    });
})();
