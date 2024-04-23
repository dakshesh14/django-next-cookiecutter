import { NextResponse, NextRequest } from "next/server";
import { cookies } from "next/headers";
// axios
import axios from "axios";

const client_id = process.env.NEXT_PUBLIC_GOOGLE_CLIENT_ID;

export async function GET(request: NextRequest) {
  const searchParams = new URLSearchParams(request.nextUrl.searchParams);

  const code = searchParams.get("code");

  try {
    const { data } = await axios.post(
      `https://oauth2.googleapis.com/token`,
      {
        code,
        client_id,
        client_secret: process.env.GOOGLE_CLIENT_SECRET,
        redirect_uri: "http://localhost:3000/api/auth/google/callback",
        grant_type: "authorization_code",
      },
      {
        headers: {
          "Content-Type": "application/json",
        },
      }
    );

    const { id_token } = data;

    const { data: response } = await axios.post(
      `${process.env.NEXT_PUBLIC_API_URL}/api/users/google-login`,
      {
        credential: id_token,
        client_id,
      }
    );

    const accessToken = response?.access_token;
    const refreshToken = response?.refresh_token;

    cookies().set("accessToken", accessToken);
    cookies().set("refreshToken", refreshToken);

    return NextResponse.redirect(new URL("/", request.url));
  } catch (e: any) {
    console.log(e);
    return NextResponse.json({
      status: "error",
      error: e?.message || "Something went wrong",
    });
  }
}
