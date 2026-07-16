import Link from 'next/link';

export default function Home() {
  return (
    <main className='flex min-h-screen flex-col items-center justify-center bg-gradient-to-b from-primary-50 to-primary-100'>
      <div className='text-center'>
        <h1 className='text-4xl font-bold text-primary-600 mb-4'>
          Electrical AI Engineering Suite
        </h1>
        <p className='text-xl text-gray-600 mb-8'>
          The ultimate AI-powered assistant for electrical engineers
        </p>
        <div className='space-x-4'>
          <Link href='/dashboard' className='px-6 py-3 bg-primary-600 text-white rounded-lg hover:bg-primary-700 transition'>
            Dashboard
          </Link>
          <Link href='/docs' className='px-6 py-3 border border-primary-600 text-primary-600 rounded-lg hover:bg-primary-50 transition'>
            Documentation
          </Link>
        </div>
      </div>
    </main>
  );
}