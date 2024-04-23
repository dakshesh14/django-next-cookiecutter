import * as z from "zod";

export const UserSchema = z.object({
  id: z.number(),
  username: z.string(),
  first_name: z.string(),
  last_name: z.string(),
  email: z.string(),
});
export type User = z.infer<typeof UserSchema>;

export const LoginResponseSchema = z.object({
  user: UserSchema,
  refresh_token: z.string(),
  access_token: z.string(),
});
export type LoginResponse = z.infer<typeof LoginResponseSchema>;

export const LoginFormData = z.object({
  email: z.string().email(),
  password: z.string(),
});
export type LoginFormData = z.infer<typeof LoginFormData>;
