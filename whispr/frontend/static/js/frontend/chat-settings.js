(function () {
    const wrapper = document.querySelector('[data-settings-menu]');
    if (!wrapper) return;

    const toggle = wrapper.querySelector('[data-settings-toggle]');
    const panel = wrapper.querySelector('[data-settings-panel]');
    if (!toggle || !panel) return;

    const setOpen = (open) => {
        toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
        panel.hidden = !open;
        wrapper.classList.toggle('is-open', open);
    };

    toggle.addEventListener('click', (event) => {
        event.stopPropagation();
        setOpen(panel.hidden);
    });

    document.addEventListener('click', (event) => {
        if (!wrapper.contains(event.target)) setOpen(false);
    });

    document.addEventListener('keydown', (event) => {
        if (event.key === 'Escape') setOpen(false);
    });
})();
