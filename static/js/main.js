
document.addEventListener('DOMContentLoaded', () => {
    // Ripple Effect (Simple version)
    const createRipple = (event) => {
        const button = event.currentTarget;
        const circle = document.createElement("span");
        const diameter = Math.max(button.clientWidth, button.clientHeight);
        const radius = diameter / 2;

        circle.style.width = circle.style.height = `${diameter}px`;
        circle.style.left = `${event.clientX - button.offsetLeft - radius}px`;
        circle.style.top = `${event.clientY - button.offsetTop - radius}px`;
        circle.classList.add("ripple");

        const ripple = button.getElementsByClassName("ripple")[0];
        if (ripple) {
            ripple.remove();
        }

        button.appendChild(circle);
    };

    const buttons = document.getElementsByClassName("btn-material");
    for (const button of buttons) {
        button.addEventListener("click", createRipple);
    }

    // Sidebar Toggle for Mobile
    const toggleBtn = document.getElementById('sidebar-toggle');
    const sidebar = document.querySelector('.sidebar');
    const overlay = document.querySelector('.overlay');

    if (toggleBtn) {
        toggleBtn.addEventListener('click', () => {
            sidebar.classList.toggle('open');
            // If we had an overlay, we'd toggle it here too
        });
    }
});
