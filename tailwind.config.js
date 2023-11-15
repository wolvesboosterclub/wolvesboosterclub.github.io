/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./*.html",
    "./holiday_party/*.html"
  ],
  safelist: [
    'max-h-0', 'max-h-max'
  ],
  theme: {
    extend: {
      boxShadow: {
        'up-lg': '0 -10px 15px -3px var(--tw-shadow-color), 0 -4px 6px -4px var(--tw-shadow-color)',
      },
      dropShadow: {
        glow: [
          "0 0px 10px var(--tw-shadow-color)",
          "0 0px 35px var(--tw-shadow-color)"
        ]
      },
      colors: {
        'half-clear-white': 'rgba(255, 255, 255, 0.5)'
      },
      transitionProperty: {
        'position': 'top, bottom, left, right'
      }
    },
  },
  plugins: [],
}

