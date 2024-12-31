import { authRequest } from '@/utils/auth';
import { NextResponse } from 'next/server';

export async function POST(request) {
    const { email, username, password } = await request.json();

    authRequest("/auth/login", "POST", { email: email, username: username, password: password })
        .then(async (response) => {
            if (response.ok) {
                const cookies = response.headers.get('set-cookie');
                if (cookies) {
                    const authSessionCookie = cookies.split(';').find(cookie => cookie.trim().startsWith('auth_session='));
                    if (authSessionCookie) {
                        const authSession = authSessionCookie.split('=')[1];
                        const response = NextResponse.json({ success: true });
                        response.cookies.set('auth_session', authSession, { httpOnly: true, secure: true, path: '/' });
                        return response;
                    }
                }

            }
            return NextResponse.json({ error: 'Failed to login' }, { status: response.status });
        });
}