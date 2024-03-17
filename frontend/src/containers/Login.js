import React, { useState } from 'react'
import { Navigate, Link } from 'react-router-dom'
import { connect } from 'react-redux'
import CSRFToken from '../components/CSRFToken'
import { login } from '../actions/auth'

const Login = ({ login, isAuthenticated }) => {
  const [formData, setFormData] = useState({
    username: '',
    password: ''
  })
  const { username, password } = formData

  const onChange = e =>
    setFormData({ ...formData, [e.target.name]: e.target.value })

  const onSubmit = e => {
    e.preventDefault()
    login(username, password)
  }

  if (isAuthenticated) {
    return <Navigate to='/dashboard' />
  }

  return (
    <div className='conatiner m-5'>
      <h1>Sign in into your Account</h1>
      <form onSubmit={e => onSubmit(e)}>
        <CSRFToken />
        <div className='form-group'>
          <label className='form-label'>Username: </label>
          <input
            className='form-control'
            type='text'
            placeholder='username'
            name='username'
            onChange={e => onChange(e)}
            value={username}
            required
          />
        </div>
        <div className='form-group mt-3'>
          <label className='form-label'>Password: </label>
          <input
            className='form-control'
            type='text'
            placeholder='password'
            name='password'
            onChange={e => onChange(e)}
            value={password}
            minLength='6'
            required
          />
        </div>
        <button className='btn btn-primary mt-3' type='submit'>
          Login
        </button>
        <p className='mt-3'>
          Don't have an Account? <Link to='/register'> Sign Up</Link>
        </p>
      </form>
    </div>
  )
}

const mapStateToProps = state => ({
  isAuthenticated: state.auth.isAuthenticated
})

export default connect(mapStateToProps, { login })(Login)
