(function () {
    var nav = document.querySelector('.site-navbar');
    if (!nav) return;
    var onScroll = function () {
        nav.classList.toggle('is-scrolled', window.scrollY > 4);
    };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
})();
