import React from 'react'
import { HomeOutline, CalendarOutline, ChartSquareBar, UserCircle } from 'heroicons-react'

export default function Sidebar () {
  return (
        <div className="sidebar-container">
          <div className="sidebar-element">
            <HomeOutline className="icon"/>
            <span>Dashboard</span>
          </div>  
          <div className="sidebar-element">
            <CalendarOutline className="icon"/>
            <span>Calendar</span>
          </div>
          <div className="sidebar-element">
            <ChartSquareBar className="icon"/>
            <span>Statistics</span>
          </div>
          <div className="sidebar-element">
            <UserCircle className="icon"/>
            <span>User</span>
          </div>
        </div>
  )
}
