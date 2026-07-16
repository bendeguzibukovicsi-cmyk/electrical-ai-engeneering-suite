"""Settings page
"""

import Header from '../../components/Header';
import Footer from '../../components/Footer';
import Card from '../../components/Card';
import Input from '../../components/Input';
import Button from '../../components/Button';

export default function Settings() {
  return (
    <div className="flex flex-col min-h-screen">
      <Header />
      
      <main className="flex-grow max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 w-full">
        <h1 className="text-3xl font-bold mb-8">Settings</h1>
        
        <Card title="Account Settings" className="max-w-md">
          <Input label="Email" type="email" placeholder="your@email.com" />
          <Input label="Full Name" placeholder="Your Name" />
          <Input label="Password" type="password" placeholder="••••••••" />
          <div className="mt-6">
            <Button>Save Changes</Button>
          </div>
        </Card>
      </main>
      
      <Footer />
    </div>
  );
}