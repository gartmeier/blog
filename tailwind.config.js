/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["blog/templates/**/*.html", "blog/static/**/*.js", "blog/**/*.py"],
  theme: {
    fontFamily: {
      sans: "Geist",
      mono: "JetBrains Mono"
    },
    extend: {},
  },
  plugins: [require("@tailwindcss/typography"), require("daisyui")],
  daisyui: {
    themes: ["light", "dark"],
  },
};
