/** @type {import('tailwindcss').Config} */

module.exports = {
    content: ["apps/**/*.{html,js}"],
    theme: {
        extend: {
            colors: {
                "blue-main": "#abcaff",
                "blue-main-light": "#e6f3ff",
                "blue-btn-default": "#80b7ff",
                "blue-btn-hover": "#60a4fc",
                "blue-btn-onclick": "#4691f2",
            },
        },
    },
    plugins: [],
};
