/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./flaskmain/templates/*.{html,js}","./node_modules/flowbite/**/*.js"],
  theme: {
    extend: {},
  },
  plugins: [
    require('@tailwindcss/forms'),
  ],
}

