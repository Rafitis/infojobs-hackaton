import { Logo } from './components/Logo'
import { JobsOffers } from './components/JobsOffers'
import './index.css'


export const metadata = {
  title: 'InfoJobs - Resumidor de ofertas de trabajo',
  description: 'Herramienta que resume las ofertas de trabajo de diferentes empresas y además te las lee con una voz muy especial.'
}

function App() {
  return (
    <>
      <header className='py-20 m-20'>
        <h1 className='flex flex-col items-center justify-center text-lg'>
          <Logo />
          <strong className='font-semibold tracking-wider text-black/80'>Resumidor de ofertas de trabajo</strong>
        </h1>
      </header>
      <main>
        <JobsOffers />
      </main>
    </>
  )
}

export default App
