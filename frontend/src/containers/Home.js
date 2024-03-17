import React from 'react'
import { Link } from 'react-router-dom'

const Home = () => {
  return (
    <div className='container'>
      <div className='mt-5 p-5 bg-light'>
        <h1 className='display-4'>Welcome to event app </h1>
        <p className='lead'>
          This is a wonder ful application where you can add an event that gonna
          happen
        </p>
        <hr className='my-4' />
        <p>Click the button below to login</p>
        <Link className='btn btn-primary btn-lg' to='/login'>
          Login
        </Link>
      </div>
    </div>
  )
}

export default Home
