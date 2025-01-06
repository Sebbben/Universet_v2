import "./globals.css";
import {NextUIProvider} from "@nextui-org/react";


export const metadata = {
  title: "Hello world",
  description: "",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        <NextUIProvider>
          {children}
        </NextUIProvider>
      </body>
    </html>
  );
}
