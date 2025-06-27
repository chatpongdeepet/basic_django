module.exports = {
  content: [
    "../templates/**/*.html", // Templates within your 'theme' app
    "../../templates/**/*.html", // Templates in other Django apps
    "../../**/*.js", // Optional: JavaScript files that might contain Tailwind classes
  ],
  plugins: {
    "@tailwindcss/postcss": {},
    "postcss-simple-vars": {},
    "postcss-nested": {},
  },
};
