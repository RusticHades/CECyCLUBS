document.addEventListener("DOMContentLoaded", () => {
    const options = {
        root: null,
        rootMargin: "0px",
        threshold: 0.1 // porcentaje visible
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            const animationClass = entry.target.getAttribute('data-animacion');

            if (entry.isIntersecting) {
                // Si es visible, aplica la clase de animación
                if (animationClass) {
                    entry.target.classList.add(animationClass);
                }
            } else {
                // Cuando deja de ser visible, quita la clase de animación para reiniciar
                if (animationClass) {
                    entry.target.classList.remove(animationClass);
                }
            }
        });
    }, options);

    // Selecciona los elementos que se desean animar
    const elementosAnimados = document.querySelectorAll('.animar');
    elementosAnimados.forEach(element => {
        observer.observe(element);
    });
});