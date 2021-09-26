import React, { Suspense } from 'react'
import Loader from './components/loader/Loader'
import Sidebar from './components/sidebar/Sidebar'
import Landing from './components/dashboard/Dashboard'
import './App.css'

function App () {
  return (
    <Suspense fallback={<Loader/>}>
      <div className="App">
        <Sidebar />
        <Landing />
      </div>
    </Suspense>

  )
}

export default App
