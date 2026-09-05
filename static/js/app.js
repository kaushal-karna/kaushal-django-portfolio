document.addEventListener("DOMContentLoaded", () => {
    const themeToggle = document.querySelector(".theme-toggle");
    const root = document.documentElement;

    const updateThemeToggle = () => {
        const isLight = root.dataset.theme === "light";
        themeToggle.setAttribute("aria-pressed", isLight);
        themeToggle.setAttribute("aria-label", isLight ? "Switch to dark mode" : "Switch to light mode");
        themeToggle.querySelector(".theme-icon").textContent = isLight ? "☾" : "☼";
        themeToggle.querySelector(".theme-label").textContent = isLight ? "Dark" : "Light";
    };

    if (themeToggle) {
        updateThemeToggle();
        themeToggle.addEventListener("click", () => {
            root.dataset.theme = root.dataset.theme === "light" ? "dark" : "light";
            localStorage.setItem("portfolio-theme", root.dataset.theme);
            updateThemeToggle();
        });
    }

    const nav = document.querySelector(".nav");
    const toggle = document.querySelector(".menu-toggle");
    if (toggle) {
        toggle.addEventListener("click", () => {
            const open = nav.classList.toggle("menu-open");
            toggle.setAttribute("aria-expanded", open);
            toggle.setAttribute("aria-label", open ? "Close navigation" : "Open navigation");
        });
        document.querySelectorAll(".nav-links a").forEach(a => {
            a.addEventListener("click", () => {
                nav.classList.remove("menu-open");
                toggle.setAttribute("aria-expanded", "false");
                toggle.setAttribute("aria-label", "Open navigation");
            });
        });
    }

    const sections = document.querySelectorAll("main section[id]");
    const navLinks = document.querySelectorAll(".nav-links a");
    const sectionObserver = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                navLinks.forEach(link => {
                    link.classList.toggle("active", link.getAttribute("href") === `#${entry.target.id}`);
                });
            }
        });
    }, {rootMargin: "-35% 0px -55%", threshold: 0});
    sections.forEach(section => sectionObserver.observe(section));

    const cursor = document.querySelector(".cursor-glow");
    window.addEventListener("pointermove", e => {
        if (cursor) {
            cursor.style.left = e.clientX + "px";
            cursor.style.top = e.clientY + "px";
        }
    });

    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add("visible");
                observer.unobserve(entry.target);
            }
        });
    }, {threshold: .12});
    document.querySelectorAll(".reveal").forEach(el => observer.observe(el));

    const filters = document.querySelectorAll(".filter");
    const cards = document.querySelectorAll(".project-card");
    const projectCount = document.querySelector(".project-count");
    filters.forEach(button => {
        button.addEventListener("click", () => {
            filters.forEach(b => b.classList.remove("active"));
            button.classList.add("active");
            const filter = button.dataset.filter;
            let visibleProjects = 0;
            cards.forEach(card => {
                const visible = filter === "all" || card.dataset.category === filter;
                card.classList.toggle("hidden", !visible);
                if (visible) visibleProjects += 1;
            });
            if (projectCount) projectCount.textContent = `${visibleProjects} project${visibleProjects === 1 ? "" : "s"}`;
        });
    });

    setTimeout(() => {
        document.querySelectorAll(".toast").forEach(t => {
            t.style.opacity = "0";
            t.style.transform = "translateY(-8px)";
            t.style.transition = ".35s";
            setTimeout(() => t.remove(), 400);
        });
    }, 4200);
});
