"use server";
export async function apiRequest(endpoint, method, data) {

    console.log(endpoint, method, data)
    
    return await fetch("http://api:3000" + endpoint, {
        method: method,
        body: JSON.stringify(data)
    })
}