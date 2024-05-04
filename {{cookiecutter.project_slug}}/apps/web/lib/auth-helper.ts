export const googleUrl = (from: string) => {
  const rootUrl = "https://accounts.google.com/o/oauth2/v2/auth";

  if (typeof window === "undefined") return rootUrl;

  const origin = window.location.origin;

  const options = {
    redirect_uri: `${origin}/api/auth/google/callback`,
    client_id: process.env.NEXT_PUBLIC_GOOGLE_CLIENT_ID!,
    access_type: "offline",
    response_type: "code",
    prompt: "consent",
    scope: [
      "https://www.googleapis.com/auth/userinfo.profile",
      "https://www.googleapis.com/auth/userinfo.email",
    ].join(" "),
    state: from,
  };

  const qs = new URLSearchParams(options).toString();

  return `${rootUrl}?${qs}`;
};
