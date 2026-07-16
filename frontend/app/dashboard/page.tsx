"""Dashboard page
"""

import Header from '../components/Header';
import Footer from '../components/Footer';
import Card from '../components/Card';
import Button from '../components/Button';

export default function Dashboard() {
  return (
    <div className="flex flex-col min-h-screen">
      <Header />
      
      <main className="flex-grow max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 w-full">
        <h1 className="text-3xl font-bold mb-8">Dashboard</h1>
        
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-8">
          <Card title="Projects">
            <p className="text-gray-600 mb-4">Manage your engineering projects</p>
            <Button>View Projects</Button>
          </Card>
          
          <Card title="Circuits">
            <p className="text-gray-600 mb-4">Design and analyze circuits</p>
            <Button>Design Circuit</Button>
          </Card>
          
          <Card title="Simulations">
            <p className="text-gray-600 mb-4">Run circuit simulations</p>
            <Button>Run Simulation</Button>
          </Card>
          
          <Card title="PCB Design">
            <p className="text-gray-600 mb-4">Create PCB layouts and schematics</p>
            <Button>Create PCB</Button>
          </Card>
          
          <Card title="Firmware">
            <p className="text-gray-600 mb-4">Generate and compile firmware</p>
            <Button>Generate Firmware</Button>
          </Card>
          
          <Card title="Documentation">
            <p className="text-gray-600 mb-4">Generate technical documentation</p>
            <Button>Generate Docs</Button>
          </Card>
        </div>
      </main>
      
      <Footer />
    </div>
  );
}