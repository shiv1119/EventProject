import React, { useState } from 'react'
import { Navigate, Link } from 'react-router-dom'
import { connect } from 'react-redux'
import { register } from '../actions/auth'
import CSRFToken from '../components/CSRFToken'

const Register = ({ register, isAuthenticated }) => {
  const [formData, setFormData] = useState({
    username: '',
    password: '',
    re_password: ''
  })

  const [accountCreated, setAccountCreated] = useState(false)
  const { username, password, re_password } = formData

  const onChange = e =>
    setFormData({ ...formData, [e.target.name]: e.target.value })

  const onSubmit = e => {
    e.preventDefault()

    if (password === re_password) {
      register(username, password, re_password)
      setAccountCreated(true)
    }
  }
  if (isAuthenticated) {
    return <Navigate to='/dashboard' />
  } else if (accountCreated) {
    return <Navigate to='/login' />
  }

  return (
    <div className='conatiner m-5'>
      <h1>Register for an account</h1>
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
        <div className='form-group mt-3'>
          <label className='form-label'>Confirm Password: </label>
          <input
            className='form-control'
            type='text'
            placeholder='re_password'
            name='re_password'
            onChange={e => onChange(e)}
            value={re_password}
            minLength='6'
            required
          />
        </div>
        <button className='btn btn-primary mt-3' type='submit'>
          Register
        </button>
        <p className='mt-3'>
          Already have account? <Link to='/login'> Sign In</Link>
        </p>
      </form>
    </div>
  )
}

const mapStateToProps = state => ({
  isAuthenticated: state.auth.isAuthenticated
})

export default connect(mapStateToProps, { register })(Register)
