import {
  Navbar,
  NavbarBrand,
  NavbarContent,
  NavbarItem,
  Link,
} from "@nextui-org/react";

export const NavBar = () => {
  return (
    <Navbar isBordered variant="sticky">
      <NavbarBrand>
        <Link href="/">
          <img src="/logo.png" alt="Logo" className="h-8 w-8" />
        </Link>
      </NavbarBrand>
      <NavbarContent>
        <NavbarItem>
          <Link
            href="/about"
            className="text-lg text-gray-700 hover:text-gray-900"
          >
            About
          </Link>
        </NavbarItem>
        <NavbarItem>
          <Link
            href="/services"
            className="text-lg text-gray-700 hover:text-gray-900"
          >
            Services
          </Link>
        </NavbarItem>
        <NavbarItem>
          <Link
            href="http://auth.localhost:3000/login"
            className="text-lg text-gray-700 hover:text-gray-900"
          >
            Login
          </Link>
        </NavbarItem>
      </NavbarContent>
    </Navbar>
  );
};
