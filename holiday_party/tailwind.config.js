/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./*.html"],
  theme: {
    extend: {
      boxShadow: {
        'up-lg': '0 -10px 15px -3px var(--tw-shadow-color), 0 -4px 6px -4px var(--tw-shadow-color)',
      }
    },
  },
  plugins: [],
}

