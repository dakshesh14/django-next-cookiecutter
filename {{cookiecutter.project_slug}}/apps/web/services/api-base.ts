import axios from "axios";

// cookie
import Cookies from "js-cookie";

const baseUrl = process.env.NEXT_PUBLIC_API_URL;

abstract class ApiBase {
  protected static async setAccessToken(accessToken: string) {
    Cookies.set("accessToken", accessToken, {
      expires: 7,
    });
  }

  protected static async setRefreshToken(refreshToken: string) {
    Cookies.set("refreshToken", refreshToken, {
      expires: 7 * 4,
    });
  }

  protected static async getAccessToken() {
    return Cookies.get("accessToken");
  }

  protected static async getRefreshToken() {
    return Cookies.get("refreshToken");
  }

  protected static async get<T>(url: string, query?: any) {
    let headers = {};

    if (await this.getAccessToken()) {
      headers = {
        Authorization: `Bearer ${await this.getAccessToken()}`,
      };
    }

    try {
      const response = await axios.get<T>(`${baseUrl}${url}`, {
        params: query,
        headers,
      });
      return response.data;
    } catch (error) {
      console.log(error);
      throw error;
    }
  }

  protected static async post<T>(url: string, data: any, _headers?: any) {
    let headers = {};

    console.log(axios);

    if (await this.getAccessToken()) {
      headers = {
        Authorization: `Bearer ${await this.getAccessToken()}`,
        ..._headers,
      };
    }

    try {
      const response = await axios.post<T>(`${baseUrl}${url}`, data, {
        headers,
      });
      return response.data;
    } catch (error) {
      console.log(error);
      throw error;
    }
  }

  protected static async patch<T>(url: string, data: any) {
    let headers = {};

    if (await this.getAccessToken()) {
      headers = {
        Authorization: `Bearer ${await this.getAccessToken()}`,
      };
    }

    try {
      const response = await axios.patch<T>(`${baseUrl}${url}`, data, {
        headers,
      });
      return response.data;
    } catch (error) {
      console.log(error);
      throw error;
    }
  }

  protected static async delete<T>(url: string) {
    let headers = {};

    if (await this.getAccessToken()) {
      headers = {
        Authorization: `Bearer ${await this.getAccessToken()}`,
      };
    }

    try {
      const response = await axios.delete<T>(`${baseUrl}${url}`, {
        headers,
      });
      return response.data;
    } catch (error) {
      console.log(error);
      throw error;
    }
  }

  protected static async postWithoutHeader<T>(url: string, data: any) {
    try {
      const response = await axios.post<T>(`${baseUrl}${url}`, data);
      return response.data;
    } catch (error) {
      console.log(error);
      throw error;
    }
  }
}

export default ApiBase;
