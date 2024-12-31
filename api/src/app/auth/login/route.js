import { NextResponse } from 'next/server';

export async function POST(request) {
    const { email, password } = await request.json();

    const res = await fetch('http://auth:3000/auth/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email, password }),
    });

    if (!res.ok) {
        return NextResponse.json({ error: 'Failed to login' }, { status: res.status });
    }

    const data = await res.json();
    return NextResponse.json(data);
}