import ApiBase from "./api-base";

// cookies
import Cookies from "js-cookie";

// import type { User, UserForm, LoginResponse } from "@/types/user";
type User = any;
type UserForm = any;
type LoginResponse = any;

class AuthenticationService extends ApiBase {
  static async login(email: string, password: string) {
    const response = await this.postWithoutHeader<LoginResponse>(
      "/api/users/login/",
      {
        email,
        password,
      }
    );

    this.setAccessToken(response.access_token);
    this.setRefreshToken(response.refresh_token);

    return response;
  }

  static async register(userForm: UserForm) {
    const response = await this.postWithoutHeader<LoginResponse>(
      "/api/users/register/",
      userForm
    );

    this.setAccessToken(response.access_token);
    this.setRefreshToken(response.refresh_token);

    return response;
  }

  static refreshToken = async () => {
    const response = await this.post<any>("/api/users/refresh-token/", {
      refresh: Cookies.get("refreshToken"),
    });
    Cookies.set("accessToken", response.access, {
      expires: 7,
    });
    return response.access;
  };

  static async getMe() {
    const response = await this.get<User>("/api/users/me/");
    return response;
  }

  static async logout() {
    const response = await this.post("/api/users/logout/", {});
    return response;
  }
}

export default AuthenticationService;
