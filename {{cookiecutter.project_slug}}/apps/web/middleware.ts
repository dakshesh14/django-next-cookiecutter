import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";

import AuthenticationService from "@/services/auth-service";

const redirect = (req: NextRequest) => {
  const url = req.nextUrl.clone();
  url.pathname = "/login";
  return NextResponse.redirect(url);
};

export const middleware = async (req: NextRequest) => {
  const accessToken = req?.cookies?.get("accessToken");
  const refreshToken = req?.cookies?.get("refreshToken");

  if (!accessToken && !refreshToken) {
    return redirect(req);
  }

  if (accessToken) {
    try {
      await AuthenticationService.getMe();
    } catch (error: any) {
      if (error?.response && error.response.status === 401) {
        try {
          const newAccessToken = await AuthenticationService.refreshToken();
          req.cookies.set("accessToken", newAccessToken);
        } catch (error) {
          return redirect(req);
        }
      }
    }
  }

  if (refreshToken) {
    try {
      await AuthenticationService.getMe();
    } catch (error: any) {
      if (error?.response && error.response.status === 401) {
        return redirect(req);
      }
    }
  }
};

export const config = {
  matcher: ["/"],
};
