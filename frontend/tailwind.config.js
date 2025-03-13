/** @type {import('tailwindcss').Config} */
export default {
    content: [
      "./index.html",
      "./src/**/*.{js,ts,jsx,tsx}",
    ],
    theme: {
      extend: {
        fontFamily: {
          sans: ['"SF Pro Display"', '-apple-system', 'BlinkMacSystemFont', '"Segoe UI"', 'Roboto', 'Helvetica', 'Arial', 'sans-serif'],
        },
        colors: {
          blue: {
            500: '#0071e3', // Apple's primary blue
            600: '#0077ed', // Slightly darker blue for hover states
          },
        },
        borderRadius: {
          'xl': '0.75rem', // Apple uses slightly larger rounded corners
        },
        boxShadow: {
          'sm': '0 1px 2px rgba(0, 0, 0, 0.05)',
        }
      },
    },
    plugins: [],
  }