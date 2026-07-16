"""Header component
"""

export default function Header() {
  return (
    <header className="bg-primary-600 text-white shadow-lg">
      <nav className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
        <div className="flex justify-between items-center">
          <div className="text-2xl font-bold">
            Electrical AI Engineering Suite
          </div>
          <div className="space-x-4">
            <a href="/" className="hover:bg-primary-700 px-3 py-2 rounded-md">
              Home
            </a>
            <a href="/dashboard" className="hover:bg-primary-700 px-3 py-2 rounded-md">
              Dashboard
            </a>
            <a href="/docs" className="hover:bg-primary-700 px-3 py-2 rounded-md">
              Docs
            </a>
          </div>
        </div>
      </nav>
    </header>
  );
}