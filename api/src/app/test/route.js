import { NextResponse } from "next/server";

export function GET(req) {
    return NextResponse.json({message: "Hello world"}, {status: 200})
}