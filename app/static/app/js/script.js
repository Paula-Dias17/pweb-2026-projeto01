const links = document.querySelectorAll(".nav-link");
const currentPage = window.location.pathname;

links.forEach(link => {
    const linkPath = link.getAttribute("href");

    if (linkPath === currentPage) {
        link.classList.add("active");
    }
});