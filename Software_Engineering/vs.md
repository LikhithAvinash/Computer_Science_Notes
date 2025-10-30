```
| Feature | GitHub Actions (The `.yml` files) | Jenkins (The `Jenkinsfile`) |
| :--- | :--- | :--- |
| **What is it?** | A **CI/CD *service*** managed by GitHub. | A **CI/CD *server*** you must host and manage. |
| **Setup** | **Nothing to install.** Just create a `.yml` file in your `.github/workflows` folder. | You must **install and configure** the Jenkins Java application on a server (like your Droplet). |
| **Maintenance** | **Zero.** GitHub manages all updates, security, and uptime for you. | **High.** You are 100% responsible for updating Jenkins, managing 1000s of plugins, and securing the server. |
| **Server Cost** | **Free** (with generous limits for public repos). The servers (runners) are provided by GitHub. | **You pay.** It runs on your Droplet, consuming your RAM and CPU 24/7, which can be expensive. |
| **Integration** | **Perfect.** It's built directly into GitHub. It knows about your PRs, code, and secrets automatically. | **External.** You must manually connect it to GitHub with webhooks and plugins. |
| **Configuration** | Written in **YAML** (`.yml` files). | Written in **Groovy** (`Jenkinsfile`). |
| **Ecosystem** | Uses the **GitHub Marketplace** for pre-built "Actions" (like the SSH action). | Uses its **Plugin Ecosystem** (1800+ plugins). Incredibly powerful but can be complex. |
| **Bottom Line** | It's a **simple, modern, and maintenance-free** tool that's perfectly integrated with your code. | It's a **powerful, flexible, and "heavy"** tool that gives you infinite control but requires a lot of work. |
```
