"""Auth service
"""

import { apiService } from './api';

export const authService = {
  async register(email: string, username: string, password: string, fullName?: string) {
    return apiService.post('/auth/register', {
      email,
      username,
      password,
      full_name: fullName,
    });
  },

  async login(email: string, password: string) {
    const response = await fetch('http://localhost:8000/api/v1/auth/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body: new URLSearchParams({
        username: email,
        password,
      }),
    });
    if (!response.ok) throw new Error('Login failed');
    return response.json();
  },

  async getCurrentUser() {
    return apiService.get('/auth/me');
  },

  logout() {
    localStorage.removeItem('token');
  },
};
