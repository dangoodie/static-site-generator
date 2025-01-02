# Static Site Generator

A **Static Site Generator** (SSG) is a tool that converts raw content files (such as Markdown and images) into a static website comprising HTML and CSS files. This project allows you to build static websites quickly, making it perfect for blogs, portfolios, documentation, and other content-heavy websites.

## 📌 Features
- Converts Markdown (`.md`) files into HTML.
- Supports images and other static assets.
- Generates lightning-fast, secure, and easily hostable websites.
- Automatically processes files in the `content` folder and links static assets from the `static` folder.
- Includes a customizable default CSS for styling.
- Ideal for blogs, portfolios, landing pages, and documentation.

## 💡 What Are Static Sites?
Static sites serve content that is pre-generated, meaning the website does not rely on a database or server-side scripting to display content. This makes them:

- **Fast**: All content is served as pre-built HTML, reducing server-side processing.
- **Secure**: Without a backend, there's no attack surface for malicious users.
- **Easy to Host**: Can be deployed on any static hosting provider (e.g., GitHub Pages, Netlify, Vercel).

### What Static Sites Can't Do
Static sites are not suitable for dynamic interactions such as:

- User logins
- File uploads
- Commenting systems
- Saving preferences

For these features, a dynamic site with server-side functionality would be required.

---

## 🗂️ Folder Structure
The project follows a straightforward folder structure to organize content and assets:

```
static-site-generator/
├── content/      # Markdown files for website content
├── static/       # Static assets like images and CSS
├── public/       # Generated HTML files
├── src/          # Source scripts, including main.py
├── main.sh       # Script to generate and host the site
```

### Folder Descriptions
- **`content/`**: Place your `.md` files here. Each file is converted into an HTML file.
- **`static/`**: This folder contains static assets such as images and CSS files. The main CSS file is `index.css` and can be customized as needed.
- **`public/`**: This folder is where the generated HTML files will be placed. It can be directly deployed to a static hosting service.
- **`src/`**: Contains source scripts, including `main.py`, which handles the generation logic.
- **`main.sh`**: A script that generates the site and serves it locally at `http://localhost:8888`.

---

## ✨ Getting Started
### Prerequisites
- Python 3.x installed on your system.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/dangoodie/static-site-generator.git
   cd static-site-generator
   ```

2. **Prepare Content**:
   - Add your Markdown files to the `content/` folder.
   - Add your custom CSS, images, or other assets to the `static/` folder. You can also use the provided default CSS (`index.css`) if no custom styles are needed.

3. **Generate and Serve the Site**:
   Run the script to generate the HTML files and host the site locally:
   ```bash
   ./main.sh
   ```

   The generated files will appear in the `public/` folder, and the site will be available at `http://localhost:8888`.

### Linking Static Assets
- Any images or other static files placed in the `static/` folder are automatically linked relative to the `public/` folder. Use standard Markdown syntax to reference these assets in your `.md` files:
  ```markdown
  ![Alt Text](images/file_name.png)
  ```

---

## 📬 Contact
If you have any questions or feedback, feel free to reach out:
- **GitHub**: [dangoodie](https://github.com/dangoodie)
- **Email**: [dan.gooden.dev@gmail.com]

