# To learn more about how to use Nix to configure your environment
# see: https://firebase.google.com/docs/studio/customize-workspace
{ pkgs, ... }: {
  # Which nixpkgs channel to use.
  channel = "unstable"; # or "unstable"

  # Use https://search.nixos.org/packages to find packages
  packages = [
    # pkgs.go
    # pkgs.python311
    # pkgs.uv
    pkgs.python313Packages.uv
    pkgs.nodejs_20
    # pkgs.nodePackages.nodemon
  ];

  # Sets environment variables in the workspace
  env = {
    PORT = "8080";
    GEMINI_API_KEY="";
    USE_VERTEX = "false";
    GOOGLE_OAUTH_CREDENTIALS="/home/user/adk-calendar/key.json";
    GOOGLE_CALENDAR_MCP_TOKEN_PATH="/home/user/adk-calendar/token.json";
  };
  idx = {
    # Search for the extensions you want on https://open-vsx.org/ and use "publisher.id"
    extensions = [
      # "vscodevim.vim"
    ];

    # Enable previews
    previews = {
      enable = true;
      previews = {
        web = {
          # Example: run "npm run dev" with PORT set to IDX's defined port for previews,
          # and show it in IDX's web preview panel
          command = ["uv" "run" "main.py"];
          manager = "web";
          env = {
            # Environment variables to set for your server
            PORT = "$PORT";
          };
        };
      };
    };

    # Workspace lifecycle hooks
    workspace = {
      # Runs when a workspace is first created
      onCreate = {
        # install-uv = "pip instal uv";
        # Example: install JS dependencies from NPM
        # npm-install = "npm install";
        uv-install = "uv sync";
      };
      # Runs when the workspace is (re)started
      onStart = {
        # Example: start a background task to watch and re-build backend code
        # watch-backend = "npm run watch-backend";
        run-docker = "docker compose up -d";
        run-mcp = "npx -y @cocal/google-calendar-mcp";
        # run-adk = "uv run main.py";
      };
    };
  };
  services = {
    docker.enable = true;
    postgres = {
      enable = true;
    };
  };
}
