"""Projects page
"""

import Header from '../../components/Header';
import Footer from '../../components/Footer';
import Card from '../../components/Card';
import Button from '../../components/Button';

export default function Projects() {
  return (
    <div className="flex flex-col min-h-screen">
      <Header />
      
      <main className="flex-grow max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 w-full">
        <div className="flex justify-between items-center mb-8">
          <h1 className="text-3xl font-bold">Projects</h1>
          <Button variant="primary">New Project</Button>
        </div>
        
        <Card>
          <p className="text-gray-600 text-center py-12">
            No projects yet. Create one to get started!
          </p>
        </Card>
      </main>
      
      <Footer />
    </div>
  );
}