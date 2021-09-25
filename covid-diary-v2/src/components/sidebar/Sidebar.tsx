import React from 'react'
import { HomeOutline, CalendarOutline, ChartSquareBar, UserCircle } from 'heroicons-react'

export default function Sidebar () {
  return (
        <div className="sidebar-container">
            <HomeOutline/>
            <CalendarOutline />
            <ChartSquareBar />
            <UserCircle />
        </div>
  )
}
