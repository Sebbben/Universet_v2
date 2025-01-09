"use client";
import { Card } from "@nextui-org/react";
import LoginForm from "./form";

export default function LoginPage() {
  return (
    <div className="flex items-center justify-center h-full">
      <Card className="p-8">
        <LoginForm />
      </Card>
    </div>
  );
}
