{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-23.05";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem
      (system: let
        pkgs = import nixpkgs { system = "${system}"; config.allowUnfree = true; };
      in
      {
        devShell = pkgs.mkShell {
          buildInputs = [
            pkgs.figlet

            pkgs.ruff

            (pkgs.python3.withPackages (pypkgs: with pypkgs; [requests frozendict pytest ruff]))
          ];

          shellHook = ''
            figlet "py-allspice"
          '';
        };
      }
    );
}
