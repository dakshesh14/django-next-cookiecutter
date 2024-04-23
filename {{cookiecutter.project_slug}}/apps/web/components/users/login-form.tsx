"use client";

import Link from "next/link";
import Image from "next/image";
import { useRouter, useSearchParams } from "next/navigation";
// react hook forms
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
// types
import { LoginFormData } from "@/app/types/user";
// services
import AuthenticationService from "@/services/auth-service";
// lib
import { cn } from "@ui/lib/utils";
import { googleUrl } from "@/lib/auth-helper";
// ui
import { Button, buttonVariants } from "@ui/components/button";
import {
  Form,
  FormControl,
  FormDescription,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@ui/components/form";
import { Input } from "@ui/components/input";
import { Label } from "@ui/components/label";

export function LoginForm() {
  const router = useRouter();

  const searchParams = useSearchParams();
  const nextUrl = searchParams.get("next");

  const form = useForm<LoginFormData>({
    resolver: zodResolver(LoginFormData),
    defaultValues: {
      email: "admin@admin.com",
      password: "123",
    },
  });

  async function onSubmit(data: LoginFormData) {
    await AuthenticationService.login(data.email, data.password)
      .then(() => {
        if (nextUrl) router.push(nextUrl);
        else router.push("/");
      })
      .catch(() => {
        form.setError("email", {
          type: "manual",
          message: "Invalid username or password",
        });
      });
  }

  return (
    <div className="w-full h-screen lg:grid lg:min-h-[600px] lg:grid-cols-2 xl:min-h-[800px]">
      <div className="flex items-center justify-center py-12">
        <Form {...form}>
          <form
            onSubmit={form.handleSubmit(onSubmit)}
            className="mx-auto grid w-[350px] gap-6"
          >
            <div className="grid gap-2 text-center">
              <h1 className="text-3xl font-bold">Login</h1>
              <p className="text-balance text-muted-foreground">
                Enter your email below to login to your account
              </p>
            </div>
            <div className="grid gap-4">
              <div className="grid gap-2">
                <FormField
                  control={form.control}
                  name="email"
                  render={({ field }) => (
                    <FormItem>
                      <FormLabel htmlFor="email">Email</FormLabel>
                      <Input
                        id="email"
                        type="email"
                        placeholder="Enter email"
                        {...field}
                      />
                      <FormMessage>
                        {form.formState.errors.email?.message}
                      </FormMessage>
                    </FormItem>
                  )}
                />
              </div>
              <div className="grid gap-2">
                <div className="flex items-center">
                  <Label htmlFor="password">Password</Label>
                  <Link
                    href="/forgot-password"
                    className="ml-auto inline-block text-sm underline"
                  >
                    Forgot your password?
                  </Link>
                </div>

                <FormField
                  control={form.control}
                  name="password"
                  render={({ field }) => (
                    <FormItem>
                      <Input
                        id="password"
                        type="password"
                        placeholder="Enter password"
                        {...field}
                      />
                      <FormMessage>
                        {form.formState.errors.password?.message}
                      </FormMessage>
                    </FormItem>
                  )}
                />
              </div>
              <Button type="submit" className="w-full">
                Login
              </Button>
              <Link
                href={googleUrl("/auth/login")}
                className={buttonVariants({
                  className: "w-full",
                  variant: "outline",
                })}
              >
                Login with Google
              </Link>
            </div>
            <div className="mt-4 text-center text-sm">
              Don&apos;t have an account?{" "}
              <Link href="#" className="underline">
                Sign up
              </Link>
            </div>
          </form>
        </Form>
      </div>
      <div className="hidden bg-muted lg:block">
        <Image
          src="/placeholder.svg"
          alt="Image"
          width="1920"
          height="1080"
          className="h-full w-full object-cover dark:brightness-[0.2] dark:grayscale"
        />
      </div>
    </div>
  );
}
