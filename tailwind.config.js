/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["blog/templates/**/*.html", "blog/**/*.py"],
  theme: {
    fontFamily: {
      sans: 'Geist'
    },
    extend: {},
  },
  plugins: [
    require("@tailwindcss/typography"),
    require("daisyui"),
  ],
  daisyui: {
    themes: ['light', 'dark']
  }
}

