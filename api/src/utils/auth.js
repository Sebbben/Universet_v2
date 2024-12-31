import { cookies } from "next/headers";


export async function authRequest(endpoint, method, body, {authCookie}) {

    const auth_session = authCookie ? authCookie : cookies.get(process.env.SESSION_COOKIE_NAME);

    return fetch(`http://auth:3000/auth/${endpoint}`, {
        method,
        headers: {
            'Content-Type': 'application/json',
            [process.env.SESSION_COOKIE_NAME]: auth_session
        },
        body: JSON.stringify(body),
    });    
}