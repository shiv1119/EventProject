import React from 'react'
import { Link } from 'react-router-dom'
import { connect } from 'react-redux'
import { logout } from '../actions/auth'

const Navbar = ({ isAuthenticated, logout }) => {
  return (
    <nav className='navbar navbar-expand-lg navbar-dark text-white bg-dark'>
      <div className='container-fluid'>
        <Link className='navbar-brand' exact to='/'>
          Event App
        </Link>
        <button
          className='navbar-toggler'
          type='button'
          data-bs-toggle='collapse'
          data-bs-target='#navbarNav'
          aria-controls='navbarNav'
          aria-expanded='false'
          aria-label='Toggle navigation'
        >
          <span className='navbar-toggler-icon'></span>
        </button>
        <div className='collapse navbar-collapse' id='navbarNav'>
          <ul className='navbar-nav'>
            <li className='nav-item'>
              <Link className='nav-link' aria-current='page' exact to='/'>
                Home
              </Link>
            </li>

            {!isAuthenticated && (
              <>
                <li className='nav-item'>
                  <Link className='nav-link' to='/register'>
                    Register
                  </Link>
                </li>
                <li className='nav-item'>
                  <Link className='nav-link' to='/login'>
                    Login
                  </Link>
                </li>
              </>
            )}
            {isAuthenticated && (
              <>
                <li className='nav-item'>
                  <Link className='nav-link' to='/dashboard'>
                    Dashboard
                  </Link>
                </li>
                <li className='nav-item'>
                  <a className='nav-link' onClick={logout} href='#!'>
                    Logout
                  </a>
                </li>
              </>
            )}

            <li className='nav-item'>
              <Link className='nav-link' aria-current='page' exact to='#'>
                Help
              </Link>
            </li>
            <li className='nav-item'>
              <div class='input-group '>
                <input
                  type='search'
                  class='form-control rounded'
                  placeholder='Search'
                  aria-label='Search'
                  aria-describedby='search-addon'
                />
                <span
                  class='input-group-text border-0 bg-white'
                  id='search-addon'
                >
                  Browse
                </span>
              </div>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  )
}

const mapStateToProps = state => ({
  isAuthenticated: state.auth.isAuthenticated
})

export default connect(mapStateToProps, { logout })(Navbar)
